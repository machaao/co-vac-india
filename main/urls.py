from main import app, machaao, dflow
from flask import request, Response
import os
import json
from .helper import custom_request_handler
from .util import get_element_message


@app.route('/')
def test():
    query = request.args.get('text')
    return dflow.send_message(query, '12334')


@app.route('/machaao/incoming', methods=["POST"])
def index():
    incoming_data = custom_request_handler(request)

    user_id = incoming_data["user_id"]
    message = incoming_data["messaging"]
    message = message[0]["message_data"]["text"]

    processed_message = dflow.send_message(message, user_id)
    
    if processed_message.action == "input.carausel":
        processed_message = get_element_message([{
            "title": "This is the title",
            "subtitle": "Only Pay Shipping & Handling Charges. Combo Offer for Machaao Users only.",
            "image_url": "https://provogue.s3.amazonaws.com/provogue-duffle1.jpg"
        }])

    print(processed_message)
    # resp = processed_message["queryResult"]["fulfillmentText"]

    payload = {
        "users": [user_id],
        "message": {"text": processed_message},
    }

    # Read more about APIs here: https://ganglia.machaao.com/api-docs/#/
    # or here https://messengerx.readthedocs.io/en/latest/ or here
    # https://github.com/machaao/machaao-py

    response = machaao.send_message(payload)

    return Response(
        mimetype="application/json",
        response=json.dumps({"success": True, "message": response.text}),
        status=200,
    )
