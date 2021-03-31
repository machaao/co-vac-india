from flask import Flask
import os
from dotenv import load_dotenv, find_dotenv

from machaao import Machaao
from main import dialogflow

load_dotenv(find_dotenv())
app = Flask(__name__)

machaao = Machaao(os.environ['MESSENGERX_API_TOKEN'], os.environ['MESSENGERX_BASE_URL'])
dflow = dialogflow.Dialogflow("newagent-bnes")

from main import urls