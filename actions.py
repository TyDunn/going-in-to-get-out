from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
rom rasa_sdk.executor import CollectingDispatcher


class FormExperience(FormAction):
    """Experience custom form action"""

    def name(self) -> Text:
        """Unique identifier of experience form"""

        return "form_experience"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["primary", "secondary", "tertiary"]
