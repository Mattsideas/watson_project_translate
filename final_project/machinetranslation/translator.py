import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']


authenticator = IAMAuthenticator('0zPGis0yramnRzxu6V49lQFLR8jtOsgdULXN_ua6n68e')
language_translator = LanguageTranslatorV3(
    version='2021-10-24',
    authenticator=authenticator
)

language_translator.set_service_url('https://api.au-syd.language-translator.watson.cloud.ibm.com/instances/6c33a9bc-1d1c-4e74-8aa0-39dc9d496104')

def english_to_french(english_text):
    #write the code here
    translation = language_translator.translate(
    text=english_text,
    model_id='en-fr').get_result()
    french_text=translation['translations'][0]['translation']
    return french_text

def french_to_english(french_text):
    #write the code here
    translation = language_translator.translate(
    text=french_text,
    model_id='fr-en').get_result()
    english_text=translation['translations'][0]['translation']
    return english_text