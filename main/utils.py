from df_template.fb_temp_lib import *


def get_message(elements: list, buttons):
    fb_temp = FacebookTemplate()
    for element in elements:
        fb_temp.add_element(element)

    if buttons:
        fb_temp["quick_replies"] = []

        for button in buttons:
            fb_temp.quick_replies.append(button)
    print(fb_temp.get_payload())
    return fb_temp.get_payload()


def get_sample_carousal():
    e1 = TemplateElement("Test #786 - Duffle Bag + 200 Machaao Credits",
                         "Only Pay Shipping & Handling Charges. Combo Offer for Machaao Users only.")
    e1.add_image_url("https://provogue.s3.amazonaws.com/provogue-duffle1.jpg")

    e2 = TemplateElement("Test #999 - Cricket Kit + 400 Machaao Credits",
                         "Only Pay Shipping & Handling Charges. Combo Offer for Machaao Users only.")
    e2.add_image_url("https://provogue.s3.amazonaws.com/provogue-duffle1.jpg")

    e3 = TemplateElement("Test #1234 - Basketball Net + 600 Machaao Credits",
                         "Only Pay Shipping & Handling Charges. Combo Offer for Machaao Users only.")
    e3.add_image_url("https://provogue.s3.amazonaws.com/provogue-duffle1.jpg")

    return get_message([e1.get_element(), e2.get_element(), e3.get_element()], None)


def get_welcome_msg():
    payload = {
        "text": "Hey! I am DialogFlow Sample Bot. Here are some sample supported commands",
        "quick_replies": [{
            "content_type": "text",
            "title": "Sample Text",
            "payload": "Sample Text"
        },
            {
            "content_type": "text",
            "title": "Sample Button",
            "payload": "Sample Button"
        },
            {
            "content_type": "text",
            "title": "Sample Image",
            "payload": "Sample Image"
        },
            {
            "content_type": "text",
            "title": "Sample Carousal",
            "payload": "Sample Carousal"
        }]
    }

    return payload


def get_sample_text():
    payload = {
        "text": "This is a sample text response"
    }

    return payload


def get_sample_button():
    payload = {
        "attachment": {
            "type": "template",
            "payload": {
                "template_type": "button",
                "text": "Hi, This is a sample button response",
                "buttons": [{
                    "title": "Hi",
                    "type": "postback",
                    "payload": "hi"
                }, {
                    "title": "Source",
                    "type": "web_url",
                    "url": "https://provogue.s3.amazonaws.com/provogue-duffle1.jpg"
                }]
            }
        }
    }

    return payload


def get_sample_image():
    payload = {
        "attachment": {
            "type": "template",
            "payload": {
                "template_type": "generic",
                "elements": [
                    {
                        "title": "This is Sample Image Response",
                        "subtitle": "Credits: 200",
                        "image_url": "https://provogue.s3.amazonaws.com/provogue-duffle1.jpg"
                    }
                ]
            }
        }
    }

    return payload
