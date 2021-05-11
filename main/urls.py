from main import app, machaao, dflow
from flask import request, Response
import os
import json
from .helper import custom_request_handler
from .utils import *
from df_template.fb_temp_lib import TemplateElement


@app.route('/machaao/incoming', methods=["POST"])
def index():
    incoming_data = custom_request_handler(request)

    user_id = incoming_data["user_id"]
    message = incoming_data["messaging"]
    message = message[0]["message_data"]["text"]

    payload = {
        "users": [user_id]
    }
    action = ""

    if message[0] == "/":
        action = message[1:]
    else:
        action = dflow.send_message(message, user_id)

    if action == "CityPin":
        payload["message"] = {
            "text": "Select the State or Enter the PIN Code",
            "quick_replies": get_state_buttons()
        }

    elif action.startswith('State'):
        state_id = action.split()
        state_id = state_id[1]

        payload["message"] = {
            "text": "Select the City or Enter the PIN Code",
            "quick_replies": get_city_buttons(state_id)
        }
    
    elif action.startswith('City'):
        city_id = action.split()
        city_id = city_id[1]
        get_avail_carousel(city_id)

    else:
        payload["message"] = get_welcome_msg()

    # resp = processed_message["queryResult"]["fulfillmentText"]

    # Read more about APIs here: https://ganglia.machaao.com/api-docs/#/
    # or here https://messengerx.readthedocs.io/en/latest/ or here
    # https://github.com/machaao/machaao-py

    response = machaao.send_message(payload)

    return Response(
        mimetype="application/json",
        response=json.dumps({"success": True, "message": response.text}),
        status=200,
    )
