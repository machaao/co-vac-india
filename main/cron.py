from main import app, machaao, CoWinAPI
from flask import request, Response
import json
from .utils import *

d = ""


@app.route('/machaao/cron', methods=["POST"])
def user_notifier():
    data = request.get_json()
    user_id = data['userId']
    resp = machaao.get_user_tags(user_id)
    user_tag_data = resp.json()
    city_id = user_tag_data["values"][0]

    msg = None

    if int(city_id) < 1000:
        msg = get_avail_carousel(city_id)
        if msg.get('text', None):
            return False
    else:
        msg = get_avail_carousel_by_pin(city_id)
        if msg.get('text', None):
            return False

    payload = {
        "users": [user_id],
        "message": msg,
        "quick_reply": {
            "content_type": "text",
            "title": "Mute",
            "payload": f"/Mute"
        }
    }
    machaao.send_message(payload)

    return True
