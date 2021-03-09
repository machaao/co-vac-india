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