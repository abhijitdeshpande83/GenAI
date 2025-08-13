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
import requests
from rasa_sdk import Action, Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher

dotenv.load_dotenv()
#
#
class ValidateMovieBookingForm(FormValidationAction):

    def name(self) -> Text:
        return "validate_movie_booking_form"
    
    def validate_zipcode(self, slot_value:Any,
                         dispatcher: CollectingDispatcher, 
                         tracker:Tracker, 
                         domain:Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        zipcode = slot_value
        zip_api_base = os.getenv("ZIPCODE_API_BASE")
        zip_url = f"{zip_api_base}/{zipcode}"

        if zipcode.isdigit() and len(zipcode) == 5:
            if requests.get(zip_url).status_code == 200:
                return {"zipcode": zipcode}
    
        dispatcher.utter_message(text="Please enter a valid zipcode")
        return {"zipcode": None}

    def convert_date(self, input_date):

        now = datetime.today().date()
        input_date = input_date.strip().lower()

        if input_date == "today" or input_date == "now" or input_date == "tonight":
            return now
        elif input_date == "tomorrow":
            return now + timedelta(days=1)
        elif input_date == "yesterday":
            return now - timedelta(days=1)    

    def validate_show_date(self, slot_value: Any,
                           dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        input_date = slot_value
        now = datetime.today().date()

        if input_date.isalpha():
            input_date = self.convert_date(input_date)
        else:
            input_date = parser.parse(input_date).date()
        
        if input_date < now:
            dispatcher.utter_message(text="Date should not be in the past.")
            return {"show_date": None}

        return {"show_date": input_date.strftime("%m/%d/%y")}
    
    def validate_show_time(self, slot_value: Any,
                           dispatcher: CollectingDispatcher,
                           tracker: Tracker,
                           domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        input_time = str(slot_value.replace(" ",""))
        now = datetime.now().time()
        parse_time = None

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
        if parse_time <= now:
            dispatcher.utter_message(text=f"That time is earlier than the current time {now.strftime('%H:%M')}. Please choose a later time.")
            return {"show_time": None}
        return {"show_time":parse_time.strftime("%H:%M")}

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
        except Exception as e:
            print(e)
            dispatcher.utter_message(text=f"Sorry, there was an error booking your movie ticket. "
                        f"Please try again later.")
