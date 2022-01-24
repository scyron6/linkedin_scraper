import requests
import json
import os
from dotenv import load_dotenv
from bs4 import BeautifulSoup

from error import AuthenticationError, HTMLError

class Scraper:
    def __init__(self):
        self.session = requests.Session()
        soup = BeautifulSoup(self.session.get('https://www.linkedin.com').text, "html.parser")
        csrf = soup.find('input', {'name': 'loginCsrfParam'}).get('value')

        load_dotenv()

        login_data = {
            'session_key': os.environ.get('LINKEDIN_USERNAME'),
            'session_password': os.environ.get('LINKEDIN_PASSWORD'),
            'loginCsrfParam': csrf
        }

        login_response = self.session.post('https://www.linkedin.com/uas/login-submit', data=login_data)
        soup = BeautifulSoup(login_response.text, "html.parser")
        title = soup.find('title').string
        if "Login" in title:
            raise AuthenticationError
        if (login_response.status_code != 200):
            raise HTMLError

    def get_contacts(self):
        contacts = []
        
        headers = {
            'accept': 'application/vnd.linkedin.normalized+json+2.1',
            'csrf-token': self.session.cookies.get('JSESSIONID')[1:-1]
        }

        params = {
            'decorationId': 'com.linkedin.voyager.dash.deco.web.mynetwork.ConnectionListWithProfile-15',
            'count': '40',
            'q': 'search',
            'sortType': 'RECENTLY_ADDED',
            'start': '0'
        }

        response = self.session.get('https://www.linkedin.com/voyager/api/relationships/dash/connections', headers=headers, params=params)

        if (response.status_code != 200):
            raise HTMLError

        connections = json.loads(response.text)
        for connection in connections.get('included'):
            if 'publicIdentifier' in connection:
                name = connection.get('firstName') + ' ' + connection.get('lastName') 
                response = self.session.get('https://www.linkedin.com/voyager/api/identity/profiles/' + connection.get('publicIdentifier') + '/profileContactInfo', headers=headers)
                contact_info = json.loads(response.text)
                email = contact_info.get('data').get('emailAddress')
                contacts.append((name, email))
                line = name + ', ' + email
                print(line)

        return contacts
