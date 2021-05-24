from df_template.fb_temp_lib import *
from main import cowin, machaao


def get_message(elements: list, buttons):
    fb_temp = FacebookTemplate()
    for element in elements:
        fb_temp.add_element(element)

    if buttons:
        payload = fb_temp.get_payload()
        payload["quick_replies"] = buttons
        return payload

    return fb_temp.get_payload()


def get_state_buttons():
    states = cowin.get_states()
    states = states["states"]

    buttons = []
    for state in states:
        buttons.append(
            {
                "content_type": "text",
                "title": state['state_name'],
                "payload": f'/State {state["state_id"]}'
            }
        )
    return buttons


def get_city_buttons(state_id):
    districts = cowin.get_districts(state_id)
    districts = districts["districts"]

    buttons = []
    for district in districts:
        buttons.append(
            {
                "content_type": "text",
                "title": district['district_name'],
                "payload": f'/City {district["district_id"]}'
            }
        )
    return buttons


def get_avail_carousel(district_id):
    availy = cowin.get_availability_by_district(district_id)
    availy = availy["centers"]

    elements = []
    for avail_data in availy:
        if avail_data["sessions"][0]["available_capacity"] != 0:
            elements.append(
                {
                    "title": f'{avail_data["name"]} | Slots: {avail_data["sessions"][0]["available_capacity"]} | {avail_data["fee_type"]} | Age: {avail_data["sessions"][0]["min_age_limit"]}+',
                    "subtitle": f'',
                    "image_url": f"https://raw.githubusercontent.com/machaao/co-vac-india/main/images/{avail_data['sessions'][0]['vaccine']}.jpg",
                    "buttons": [{
                        "title": "View Details",
                        "type": "web_url",
                        "url": f"https://co-vac-webview.vercel.app/vaccines/india/city/{district_id}"
                    }]
                }
            )
    if len(elements) > 0:
        attachment = {
            "type": "template",
            "payload": {
                "template_type": "generic",
                "elements": elements
            }
        }
        return {"attachment": attachment}

    return {"text": "No Slots Available In Your City"}


def get_avail_carousel_by_pin(pin):
    availy = cowin.get_availability_by_pincode(pin_code=pin)
    availy = availy["centers"]

    elements = []
    for avail_data in availy:
        if avail_data["sessions"][0]["available_capacity"] != 0:
            elements.append(
                {
                    "title": f'{avail_data["name"]} | Slots: {avail_data["sessions"][0]["available_capacity"]} | {avail_data["fee_type"]} | Age: {avail_data["sessions"][0]["min_age_limit"]}+',
                    "subtitle": f'',
                    "image_url": f"https://raw.githubusercontent.com/machaao/co-vac-india/main/images/{avail_data['sessions'][0]['vaccine']}.jpg",
                    "buttons": [{
                        "title": "View Details",
                        "type": "web_url",
                        "url": f"https://co-vac-webview.vercel.app/vaccines/india/city/{pin}"
                    }]
                }
            )
    if len(elements) > 0:
        attachment = {
            "type": "template",
            "payload": {
                "template_type": "generic",
                "elements": elements
            }
        }
        return {"attachment": attachment}

    return {"text": "No Slots Available In Your City"}


def get_welcome_msg():
    payload = {
        "text": "Hey! I am Co-Vac Bot. Get and set remainder on vaccination details by talking to me",
        "quick_replies": [{
            "content_type": "text",
            "title": "Get Info By City/Pin ℹ️",
            "payload": "/CityPin"
        }, {
            "content_type": "text",
            "title": "Notify Me 🔔",
            "payload": "/NotifyMe"
        }, {
            "content_type": "text",
            "title": "Mute 🤫",
            "payload": "/Mute"
        }]
    }

    return payload


def register_user_notify():
    payload = {
        "text": "You will be notified when there is a slot available at your location 😃"
    }

    return payload


def get_quick_reply_after_avail(city_id, pin):
    qr = []

    if city_id:
        qr = [{
            "content_type": "text",
            "title": "Set Notification",
            "payload": f"/SetNotif City {city_id}"
        }]
        # , {
        #     "content_type": "url",
        #     "title": "View Details",
        #     "payload": f"https://co-vac-webview.vercel.app/vaccines/india/city/{city_id}"
        # }
        # ]

    else:
        qr = [{
            "content_type": "text",
            "title": "Set Notification",
            "payload": f"/SetNotif PIN {pin}"
        }]
        # {
        #     "content_type": "url",
        #     "title": "View Details",
        #     "payload": f"https://co-vac-webview.vercel.app/vaccines/india/city/{pin}"
        # }]

    return qr


def user_subscribe(city_id, city_name, user_id):
    tag_payload = {
        "tag": "city",
        "status": 1,
        "values": [city_id],
        "displayName": city_name
    }
    machaao.set_tag_to_user(tag_payload, user_id)

    task_endpoint = '/v1/tasks/' + user_id
    task_payload = {
        "function": "machaao/cron",
	    "frequency": "0 0/1 * 1/1 * ? *",
        "status": -1
    }
    machaao.send_request(task_endpoint, task_payload)


def user_unsubscribe(user_id):
    untag_endpoint = "/v1/users/tag/" + user_id
    untag_payload = {
        "tag": "city",
        "statue": 0
    }
    machaao.send_request(untag_endpoint, untag_payload)

    task_endpoint = "/v1/tasks/" + user_id
    task_payload = {
        "function": "machaao/cron",
	    "frequency": "0 0/1 * 1/1 * ? *",
        "status": 1
    }

    machaao.send_request(task_endpoint, task_payload)