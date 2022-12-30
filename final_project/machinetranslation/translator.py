import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

def englishToFrench(englishText):
    language_translator.set_service_url('url')
    frenchtext = language_translator.translate(
       text="hello,how are you today?",
       model_id="en-fr" ).get_result()
    return frenchText

def frenchToEnglish(frenchText):
    language_translator.set_service_url('url')
    englishtext = language_translator.translate(
       text="Bonjour comment vas tu aujourd'hui?",
       model_id="fr-en" ).get_result()
    return englishText

   