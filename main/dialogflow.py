import requests
import json
from google.cloud import dialogflow


class Dialogflow:
    def __init__(self, AUTH_TOKEN, PROJECT_ID, SESSION_ID):
        self.AUTH_TOKEN = AUTH_TOKEN
        self.PROJECT_ID = PROJECT_ID
        self.SESSION_ID = SESSION_ID
        self.URL = f"https://dialogflow.googleapis.com/v2/projects/{PROJECT_ID}/agent/sessions/{SESSION_ID}:detectIntent"

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
        print("Query text: {}".format(response.query_result.query_text))
        print(
            "Detected intent: {} (confidence: {})\n".format(
                response.query_result.intent.display_name,
                response.query_result.intent_detection_confidence,
            )
        )
        return response.query_result.fulfillment_text
