# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
import time
from datetime import datetime, timedelta
from dateutil import parser
from rasa_sdk import Action, Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
#
#
class ValidateMovieBookingForm(FormValidationAction):

    def name(self) -> Text:
        return "validate_movie_booking_form"
    
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

        return {"show_date": input_date.strftime("%m/%d")}
