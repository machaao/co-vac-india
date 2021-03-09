from flask import Flask
import os
from dotenv import load_dotenv, find_dotenv

from machaao import Machaao
from main import dialogflow

load_dotenv(find_dotenv())
app = Flask(__name__)

machaao = Machaao(os.environ['MESSENGERX_API_TOKEN'], os.environ['MESSENGERX_BASE_URL'])
dflow = dialogflow.Dialogflow(os.environ['DIALOGFLOW_AUTH_TOKEN'], "quickstart-1597051402392", "922d370a-3082-2e71-20a6-77b89167a27a")

from main import urls