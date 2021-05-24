from main import app, machaao, dflow
from flask import request, Response
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

    print(user_id)

    payload = {
        "users": [user_id]
    }
    action = ""

    if message[0] == "/":
        action = message[1:]

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

            payload["message"] = get_avail_carousel(city_id)
            payload["message"]["quick_replies"] = get_quick_reply_after_avail(
                city_id, None)

        elif action.startswith('SetNotif'):
            action = action.split()

            loc_type = action[1]
            loc = action[2]
            user_subscribe(loc, loc_type, user_id)
            payload["message"] = register_user_notify()
        
        elif action.startswith('Mute'):
            user_unsubscribe(user_id)
            payload["message"] = {
                "text": "Now, we won't send you any notification.",
            }


        elif action.startswith('NotifyMe'):
            payload["message"] = {
                "text": "Select the State or Enter the PIN Code",
                "quick_replies": get_state_buttons()
            }
        


    else:
        action = dflow.send_message(message, user_id)

        if action.intent.display_name == "getAvailByPin":
            pin = action.parameters.__getitem__("zip-code")

            payload["message"] = get_avail_carousel_by_pin(pin)
            payload["message"]["quick_replies"] = get_quick_reply_after_avail(
                None, pin)
        
        elif action.intent.display_name == "muteNotif":
            user_unsubscribe(user_id)
            payload["message"] = {
                "text": "Now, we won't send you any notification.",
            }
        
        elif action.intent.display_name == "setNotif":
            payload["message"] = {
                "text": "Select the State or Enter the PIN Code",
                "quick_replies": get_state_buttons()
            }

        else:
            payload["message"] = get_welcome_msg()

    # resp = processed_message["queryResult"]["fulfillmentText"]

    # Read more about APIs here: https://ganglia.machaao.com/api-docs/#/
    # or here https://messengerx.readthedocs.io/en/latest/ or here
    # https://github.com/machaao/machaao-py

    # print(payload)

    response = machaao.send_message(payload)

    return Response(
        mimetype="application/json",
        response=json.dumps({"success": True, "message": response.text}),
        status=200,
    )
