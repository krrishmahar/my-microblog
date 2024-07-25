import requests
from flask import current_app
from flask_babel import _

def translate(text, source_language, dest_language):
    if 'GOOGLE_API_KEY' not in current_app.config or \
            not current_app.config['GOOGLE_API_KEY']:
        return _('Error: the translation service is not configured.')

    api_key = current_app.config['GOOGLE_API_KEY']
    url = f'https://translation.googleapis.com/language/translate/v2?key={api_key}'
    params = {
        'q': text,
        'source': source_language,
        'target': dest_language,
    }
    
    response = requests.post(url, params=params, json=[{'format':text}])
    if response.status_code != 200:
        return _('Error: the translation service failed. {}').format(response.status_code)
    return response.json()[0]['translations'][0]['text']
