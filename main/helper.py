import json
import jwt
import os
import random

_f = open(os.getcwd() + "/main/actions.json")

actions = json.load(_f)


def custom_request_handler(request):
    api_token = request.headers["api_token"]
    user_id = request.headers["user_id"]

    request.data = json.loads(request.data)

    raw = request.data.get("raw", "")

    if raw != "":
        input = jwt.decode(str(raw), api_token, algorithms=["HS512"])
        sub = input.get("sub", None)
        # print("Conditional")
        if sub and type(sub) is dict:
            sub = json.dumps(sub)

        if sub:
            decoded = json.loads(sub)
            messaging = decoded.get("messaging", None)

            return {
                "api_token": api_token,
                "user_id": user_id,
                "messaging": messaging
            }


def get_trait(wit_response):
    wit_response = wit_response.get('traits', None)
    if not wit_response:
        return False
    trait = wit_response.keys()
    trait = list(trait)[0]
    return trait, wit_response[trait][0]["confidence"]

def get_chatbot_response(wit_res):
    try:
        _res = random.choice(actions.get(wit_res[0]))
    except TypeError:
        _res = "I am still learning, didn't get you, Sorry :)"
    return _res