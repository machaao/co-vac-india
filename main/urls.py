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

    action = dflow.send_message(message, user_id)

    payload = {
        "users": [user_id]
    }
    
    if action == "Carousal":
        payload["message"] = get_sample_carousal()
    
    elif action == "Welcome":
        payload["message"] = get_welcome_msg()
    
    elif action == "Text":
        payload["message"] = get_sample_text()
    
    elif action == "Button":
        payload["message"] = get_sample_button()
    
    elif action == "Image":
        payload["message"] = get_sample_image()

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
