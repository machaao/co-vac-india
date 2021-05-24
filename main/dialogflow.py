import requests
import json
from google.cloud import dialogflow
from google.protobuf.json_format import MessageToDict


class Dialogflow:
    def __init__(self, PROJECT_ID):
        self.PROJECT_ID = PROJECT_ID

    def send_message(self, text, user_id, language_code="en"):

        session_client = dialogflow.SessionsClient()

        session = session_client.session_path(self.PROJECT_ID, user_id)
        print("Session path: {}\n".format(session))

        text_input = dialogflow.TextInput(text=text, language_code=language_code)

        query_input = dialogflow.QueryInput(text=text_input)

        response = session_client.detect_intent(
            request={"session": session, "query_input": query_input}
        )

        print("=" * 20)
        print(
            "Detected intent: {} (confidence: {})\n".format(
                response.query_result.intent.display_name,
                response.query_result.intent_detection_confidence,
            )
        )

        return response.query_result
