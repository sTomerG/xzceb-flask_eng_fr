import os

from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

def create_translator():
    """ Initiates translator"""
    authenticator = IAMAuthenticator(apikey)

    language_translator = LanguageTranslatorV3(
        version='2022-01-01',
        authenticator=authenticator)

    language_translator.set_service_url(url)
    return language_translator

def english_to_french(english_text):
    """ Uses IBM Watson to translate english text to french """
    french_text = language_translator.translate(
        text=english_text,
        model_id='en-fr').get_result()
    return french_text['translations'][0]['translation']

def french_to_english(french_text):
    """ Uses IBM Watson to translate french text to english """
    english_text = language_translator.translate(
        text=french_text,
        model_id='fr-en').get_result()
    return english_text['translations'][0]['translation']

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

language_translator = create_translator()