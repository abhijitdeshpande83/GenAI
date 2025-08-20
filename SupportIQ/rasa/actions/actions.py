# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
import time
import os
from datetime import datetime, timedelta
from dateutil import parser
from smtplib import SMTP
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import dotenv
from fuzzywuzzy import process
import requests
import psycopg2
from rasa_sdk import Action, Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, FollowupAction, ActiveLoop, AllSlotsReset


dotenv.load_dotenv()
#
#
class ValidateMovieBookingForm(FormValidationAction):

    def __init__(self):
        super().__init__()
        self.cache_response = {}

    def name(self) -> Text:
        return "validate_movie_booking_form"

    def fetch_movies(self,zipcode:Any, start_date:Any=None):

        api_key = os.getenv("MOVIE_API_KEY")
        url = os.getenv("MOVIE_BASE_URL")
        headers = {"Content-Type":"application/json"}

        params =  {"startDate":start_date, 
                   "zip":zipcode, 
                   "radius":"10", 
                   "api_key":api_key}

        response = requests.get(url, params=params, headers=headers)
        movies = response.json()
    
        return movies

    def get_time(self, showtime):
        return datetime.fromisoformat(showtime).strftime("%H:%M") 

    def search_movie(self,zipcode:Any,dispatcher:CollectingDispatcher):

        start_date = datetime.today().date()
        movies = self.fetch_movies(zipcode,start_date) 

        self.cache_response[zipcode] = movies
        self.cache_response["start_date"] = start_date
        
        if not movies:
            dispatcher.utter_message(text="No movies found near your area. Please try a different zipcode.")
            return []
        
        search_results = set([movie.get("title") for movie in movies])
        nearby_movies = '\n'.join((f"-> {movie}" for movie in search_results))
        dispatcher.utter_message(text=f"Here are movies: \n{nearby_movies}")
        return []
    
    def find_best_match(self, user_input, valid_values, tracker:Tracker):

        value_set = set(valid_values)
        best_match, score = process.extractOne(user_input, value_set)
        if score > 80:
            return best_match
        else:
            return None

    def validate_movie_name(self, slot_value:Any,
                        dispatcher:CollectingDispatcher,
                        tracker:Tracker,
                        domain: Dict[Text, Any]) -> Dict[Text, Any]:
                      
        zipcode = tracker.get_slot("zipcode")

        movies = self.cache_response[zipcode]    
        if not movies:
            dispatcher.utter_message(text=f"There are no theaters nearby {zipcode}")
            return {"movie_name": None}
        
        movies_list = [movie.get('title') for movie in movies]
        movie_name = self.find_best_match(slot_value, movies_list, tracker)
        
        if not movie_name:
            dispatcher.utter_message(text=f"Movie {slot_value} not found")
            return {"movie_name": None}

        # Find theaters having user given movie name
        movie_metadata = next((movie for movie in movies if movie.get('title')==movie_name), None)
        theaters = set([theater.get("theatre").get("name") for theater in movie_metadata.get("showtimes")])
        nearby_theaters = '\n'.join(f"-> {theater}" for theater in theaters)
        self.cache_response["movie_metadata"] = [movie_metadata]
        self.cache_response["theaters"] = theaters

        dispatcher.utter_message(text=f"Here are theaters near you for {slot_value}: \n{nearby_theaters}")
        return {"movie_name": movie_name}
        

    def validate_zipcode(self, slot_value:Any,
                         dispatcher: CollectingDispatcher, 
                         tracker:Tracker, 
                         domain:Dict[Text, Any]) -> Dict:
        print(f"validate_zipcode running {slot_value}")
        zipcode = slot_value
        zip_api_base = os.getenv("ZIPCODE_API_BASE")
        zip_url = f"{zip_api_base}/{zipcode}"

        if zipcode.isdigit() and len(zipcode) == 5:
            if requests.get(zip_url).status_code == 200:
                self.search_movie(zipcode,dispatcher)
                return {"zipcode": zipcode}
        dispatcher.utter_message(text="Please enter a valid zipcode")
        return {"zipcode": None}

    def convert_date(self, input_date):

        now = datetime.today()
        input_date = input_date.strip().lower()

        if input_date == "today" or input_date == "now" or input_date == "tonight":
            return now
        elif input_date == "tomorrow":
            return now + timedelta(days=1)
        elif input_date == "yesterday":
            return now - timedelta(days=1)    

    def validate_theater_name(self, slot_value:Any,
                              dispatcher:CollectingDispatcher,
                              tracker:Tracker,
                              domain:Dict[Text, Any]) -> Dict:

        zipcode = tracker.get_slot("zipcode")
        movie_name = tracker.get_slot("movie_name")
        
        movies = self.cache_response[zipcode]
        movie_metadate = self.cache_response["movie_metadata"]
        theaters = self.cache_response["theaters"]
        theater_name = self.find_best_match(slot_value, theaters, tracker)

        if not theater_name:
            dispatcher.utter_message(text=f"Theater {slot_value} not found")
            return {"theater_name": None}
        return {"theater_name": theater_name.strip()}
              
    def validate_show_date(self, slot_value: Any,
                           dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        input_date = slot_value
        now = datetime.today().date()

        if input_date.isalpha():
            input_date = self.convert_date(input_date)
        else:
            input_date = parser.parse(input_date)
        
        if input_date.date() < now:
            dispatcher.utter_message(text="Date should not be in the past.")
            return {"show_date": None}
        
               
        theater_name = tracker.get_slot('theater_name')
        movie_name = tracker.get_slot('movie_name')
        movie_metadata = self.cache_response.get("movie_metadata") 
      
        if input_date.date() == now:
                         
           showTime = [showtime.get("dateTime") for movie in movie_metadata for showtime in movie.get("showtimes")
                                    if showtime.get("theatre", {}).get("name")==theater_name]
           
           showTime = '\n'.join([self.get_time(showtime) for showtime in showTime])

           dispatcher.utter_message(text=f"Here are the showtimes for {theater_name} on {input_date.strftime('%m/%d/%y')}: \n{showTime}")

        else:
            movies = self.fetch_movies(tracker.get_slot("zipcode"), input_date.date())

            showTime = [showtime.get("dateTime") for movie in movies if movie.get('title')==movie_name 
                                    for showtime in movie.get("showtimes")
                                    if showtime.get("theatre").get("name")==theater_name]
            
            showTime = '\n'.join([self.get_time(showtime) for showtime in showTime])
        
            dispatcher.utter_message(text=f"Here are the showtimes for {theater_name} on {input_date.strftime('%m/%d/%y')}: \n{showTime}")

        return {"show_date": input_date.strftime("%m/%d/%y")}
    
    def validate_show_time(self, slot_value: Any,
                           dispatcher: CollectingDispatcher,
                           tracker: Tracker,
                           domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        input_time = str(slot_value.replace(" ",""))
        now = datetime.now().time()
        parse_time = None
        show_date_str = tracker.get_slot("show_date")
        show_date = datetime.strptime(show_date_str, "%m/%d/%y").date()
        curr_day = datetime.today().date()
        time_format = {
            "%I:%M%p",          # 12hrs with mons 10:15 pm/am
            "%I%p",             # 12hrs no mins 10 pm/am
            "%H:%M",            # 24hrs with mins
            "%H"                # 24hrs no mins
        }
        
        for format in time_format:
            try:
                parse_time = datetime.strptime(input_time, format).time()
            except ValueError:
                continue
        if parse_time is None:
            dispatcher.utter_message(text="Please enter a valid time")
            return {"show_time": None}
        elif parse_time <= now and show_date==curr_day:
            dispatcher.utter_message(text=f"That time is earlier than the current time {now.strftime('%H:%M')}. Please choose a later time.")
            return {"show_time": None}
        
        dispatcher.utter_message(
            text="Please select seat",
            image="https://www.rateyourseats.com/assets/images/seating_charts/static/dolby-theatre-seating-chart.jpg"
            )

        return {"show_time":parse_time.strftime("%H:%M")}

    def validate_seat_number(self, slot_value:Any,
                             dispatcher:CollectingDispatcher,
                             tracker:Tracker,
                             domain:Dict[Text, Any]) -> Dict:

        seat_number = slot_value.capitalize()
        movie_name = tracker.get_slot("movie_name")
        show_date = tracker.get_slot("show_date")
        show_time = tracker.get_slot("show_time")
        theater_name = tracker.get_slot("theater_name")

        conn = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            port=os.getenv("DB_PORT")
        )

        cur = conn.cursor()
        cur.execute("SELECT seat_number FROM movie_booking WHERE movie_name = %s AND show_date = %s AND show_time = %s AND theater_name = %s",
                    (movie_name, show_date, show_time, theater_name))
        booked_seats = cur.fetchall()
        cur.close()
        conn.close()

        booked_seats = {seat[0] for seat in booked_seats}

        if seat_number in booked_seats:
            dispatcher.utter_message(text=f"Seat {seat_number} is already booked. Please choose another seat.")
            return {"seat_number": None}
        return {"seat_number": seat_number}

class ActionSendEmail(Action):

    def name(self) -> Text:
        return "action_send_email"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text,Any]) -> List[Dict[Text,Any]]:

        SMTP_SERVER = "smtp.gmail.com"
        SMTP_PORT = 587 
        order_number = int(time.time())
        
        movie_name = tracker.get_slot("movie_name")
        show_date = tracker.get_slot("show_date")
        show_time = tracker.get_slot("show_time")
        seat_number = tracker.get_slot("seat_number")
        usr_email = tracker.get_slot("user_email")
        
        from_addr = os.getenv("EMAIL_HOST_USER")
        password = os.getenv("EMAIL_HOST_PASSWORD")

        with open("booking_confirmation.html", "r") as f:
            body_template = f.read()

        body_template = body_template.format(
            order_number=order_number,
            movie_name=movie_name,
            show_date=show_date,
            show_time=show_time,
            seat_number=seat_number
        )
        
        subject = f"Your Premier Movieplex Order Number {order_number} from {show_date}"

        msg = MIMEMultipart("alternative")
        msg["From"] = from_addr
        msg["To"] = usr_email
        msg['Subject'] = subject

        part = MIMEText(body_template, "html")
        msg.attach(part)

        # msg = f"Subject: {subject}\n\n{body_template}"

        try:
            with SMTP(SMTP_SERVER, SMTP_PORT) as server:
                server.starttls()
                server.login(from_addr, password)
                server.sendmail(from_addr, usr_email, msg.as_string())
            dispatcher.utter_message(text=f"Your booking for '{movie_name}' on {show_date} at {show_time} "\
                    f"is confirmed! A confirmation email has also been sent to {usr_email}. Enjoy the movie!")
            return  [FollowupAction('action_seat_book')]
        except Exception as e:
            print(e)
            dispatcher.utter_message(text=f"Sorry, there was an error booking your movie ticket. "
                        f"Please try again later.")
            return  []

class ActionResetMovieForm(Action):

    def name(self) -> Text:
        return "action_reset_movie_form"
    
    def run(self, dispatcher:CollectingDispatcher,
            tracker:Tracker,
            domain: Dict[Text,Any]) -> List[Dict[Text,Any]]:

        dispatcher.utter_message(text="No worries. We can stop here. Let me know if you want to start over.")
        return [AllSlotsReset(), ActiveLoop(None),
                FollowupAction("action_listen")]

class ActionSeatBook(Action):

    def name(self) -> Text:
        return "action_seat_book"
    
    def run(self, dispatcher:CollectingDispatcher,
            tracker:Tracker,
            domain: Dict[Text,Any]) -> List[Dict[Text,Any]]:
        
        movie_name = tracker.get_slot("movie_name")
        theater_name = tracker.get_slot("theater_name")
        show_date_str = tracker.get_slot("show_date")
        show_time_str = tracker.get_slot("show_time")
        seat_number = tracker.get_slot("seat_number")   
        show_date = datetime.strptime(show_date_str, "%m/%d/%y").date()
        show_time = datetime.strptime(show_time_str, "%H:%M").time()

        db_connct = psycopg2.connect(
            dbname=os.getenv("DB_NAME"),
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            port=os.getenv("DB_PORT")
            )
            
        cur = db_connct.cursor()
        query = """INSERT INTO movie_booking (movie_name, theater_name, show_date, show_time, seat_number) 
        VALUES (%s, %s, %s, %s, %s)"""

        cur.execute(query, (movie_name, theater_name, show_date, show_time, seat_number))
        db_connct.commit()  
        cur.close()
        db_connct.close()

        return []