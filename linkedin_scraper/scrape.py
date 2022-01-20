import requests
import json
from bs4 import BeautifulSoup

from info import data, get_headers, get_params

def get_contacts():
    contacts = []

    s = requests.Session()
    soup = BeautifulSoup(s.get('https://www.linkedin.com').text, "html.parser")
    csrf = soup.find('input', {'name': 'loginCsrfParam'}).get('value')
    data['loginCsrfParam'] = csrf

    s.post('https://www.linkedin.com/uas/login-submit', data=data)

    get_headers['csrf-token'] = s.cookies.get('JSESSIONID')[1:-1]
    response = s.get('https://www.linkedin.com/voyager/api/relationships/dash/connections', headers=get_headers, params=get_params)

    connections = json.loads(response.text)
    for connection in connections.get('included'):
        if 'publicIdentifier' in connection:
            name = connection.get('firstName') + ' ' + connection.get('lastName') 
            response = s.get('https://www.linkedin.com/voyager/api/identity/profiles/' + connection.get('publicIdentifier') + '/profileContactInfo', headers=get_headers)
            contact_info = json.loads(response.text)
            email = contact_info.get('data').get('emailAddress')
            contacts.append((name, email))
            line = name + ', ' + email
            print(line)

    return contacts
