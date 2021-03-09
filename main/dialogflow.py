import requests
import json


class Dialogflow:
    def __init__(self, AUTH_TOKEN, PROJECT_ID, SESSION_ID):
        self.AUTH_TOKEN = AUTH_TOKEN
        self.PROJECT_ID = PROJECT_ID
        self.SESSION_ID = SESSION_ID
        self.URL = f"https://dialogflow.googleapis.com/v2/projects/{PROJECT_ID}/agent/sessions/{SESSION_ID}:detectIntent"

    def send_message(self, message, lang="en"):
        headers = {
            "Content-Type": "application/json; charset=utf-8",
            "Authorization": f"Bearer {self.AUTH_TOKEN}",
        }

        data = {
            "queryInput": {
                "text": {
                    "text": message,
                    "languageCode": lang
                }
            }
        }

        _resp = requests.post(self.URL, headers=headers, data=json.dumps(data)) 

        return _resp.json()
