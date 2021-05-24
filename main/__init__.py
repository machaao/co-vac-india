from flask import Flask
import os
from dotenv import load_dotenv, find_dotenv

from machaao import Machaao
from main import dialogflow
from cowin_api import CoWinAPI


load_dotenv(find_dotenv())
app = Flask(__name__)


cowin = CoWinAPI()
machaao = Machaao(os.environ['MESSENGERX_API_TOKEN'],
                  os.environ['MESSENGERX_BASE_URL'])
dflow = dialogflow.Dialogflow(os.environ['PROJECT_ID'])


from main import urls, cron
