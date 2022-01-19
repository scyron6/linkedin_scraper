import os
from dotenv import load_dotenv

load_dotenv()

LINKEDIN_USERNAME = os.environ.get('LINKEDIN_USERNAME')
LINKEDIN_PASSWORD = os.environ.get('LINKEDIN_PASSWORD')

data = {
    'session_key': LINKEDIN_USERNAME,
    'session_password': LINKEDIN_PASSWORD,
}

get_headers = {
    'accept': 'application/vnd.linkedin.normalized+json+2.1',
}

get_params = {
    'decorationId': 'com.linkedin.voyager.dash.deco.web.mynetwork.ConnectionListWithProfile-15',
    'count': '40',
    'q': 'search',
    'sortType': 'RECENTLY_ADDED',
    'start': '0'
}