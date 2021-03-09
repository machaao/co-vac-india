import requests
import json

headers = {
    "Content-Type": "application/json; charset=utf-8",
    "Authorization": "Bearer ya29.a0AfH6SMA0BqcIps94VrOSWbfeGyxuk3jV78f54Lh5Au8BI2ZokxnFADotuD_G4K0aECEGg4CMDzS0M78WAJMVH79xlUhp_4P5LkjlJMly0UnTvb-df5bmJYW8Ruk6yLyfOdAv1jNd2FM-i-deBOKK8HrXz7TxlilzKhshzQeZe-6vDA9pPO97URpQmY73taFrdSmAHxo3VPC1syS3y2cg95L5eHPtz6Z6m3OohXggharjIA",
}

data = {
    "queryInput": {
        "text": {
            "text": "hi",
            "languageCode": "en"
        }
    }
}

response = requests.post(
    "https://dialogflow.clients6.google.com/v2/projects/quickstart-1597051402392/agent/sessions/922d370a-3082-2e71-20a6-77b89167a27a:detectIntent",
    headers=headers,
    data=json.dumps(data),
)

print(response.text)
