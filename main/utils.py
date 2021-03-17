def get_element_message(elements: list, buttons: list = []):
    payload = {
        "template_type": "generic",
        "elements": []
    }
    for (element, button) in zip(elements, buttons):
        to_append = {
            "title": element.title,
            "type": element.type,
            "payload": element.payload,
            "buttons": [
                {
                    "title": button.title,
                    "type": button.type,
                    "payload": button.payload
                }
            ]
        }
        payload["elements"].append(to_append)

    return {
        "attachment": {
            "type": "template",
            "payload": payload
        }
    }
