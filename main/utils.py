from df_template.fb_temp_lib import *


def get_message(elements: list, buttons):
    fb_temp = FacebookTemplate()
    for element in elements:
        fb_temp.add_element(element)

    if buttons:
        payload = fb_temp.get_payload()
        payload["quick_replies"] = buttons
        return payload

    return fb_temp.get_payload()


def get_sample_carousal():
    e1 = TemplateElement("Carousal #1 - Bird Graffiti",
                         "Carousal test image")
    e1.add_image_url(
        "https://static.remove.bg/sample-gallery/graphics/bird-thumbnail.jpg")

    e2 = TemplateElement("Carousal #2 - Green Bird",
                         "Carousal test image")
    e2.add_image_url(
        "https://4.img-dpreview.com/files/p/E~TS590x0~articles/3925134721/0266554465.jpeg")

    e3 = TemplateElement("Test #1234 - Basketball Net + 600 Machaao Credits",
                         "Carousal test image")
    e3.add_image_url(
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRmSzc_znLHt_nbXtsMQgkSO-T0iUpMFrRLTYnjcC4MPIORfC3qd7lQObuaWf6qCOWrRXU&usqp=CAU")

    buttons = []

    buttons.append(
        {
            "content_type": "text",
            "title": "Sample Text",
            "payload": "Sample Text"
        }
    )
    buttons.append(
        {
            "content_type": "text",
            "title": "Sample Button",
            "payload": "Sample Button"
        }
    )
    buttons.append(
        {
            "content_type": "text",
            "title": "Sample Image",
            "payload": "Sample Image"
        }
    )
    buttons.append(
        {
            "content_type": "text",
            "title": "Sample Carousal",
            "payload": "Sample Carousal"
        }
    )

    return get_message([e1.get_element(), e2.get_element(), e3.get_element()], buttons)


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
        "text": "This is a sample text response",
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
                    "url": "https://image.shutterstock.com/image-vector/sample-stamp-grunge-texture-vector-260nw-1389188336.jpg"
                }]
            }
        },
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
                        "image_url": "https://image.shutterstock.com/image-vector/sample-stamp-grunge-texture-vector-260nw-1389188336.jpg"
                    }
                ]
            }
        },
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
