#s4nt14g00901
import random
import os
import requests
from datetime import datetime
import json

def authenticate():
    link = 'https://www.instagram.com/accounts/login/'
    login_url = 'https://www.instagram.com/accounts/login/ajax/'

    time = int(datetime.now().timestamp())
    response = requests.get(link)
    csrf = response.cookies['csrftoken']
    password = ''

    payload = {
        'username': 'pevitt',
        'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{time}:{password}',
        'queryParams': {},
        'optIntoOneTap': 'false'
    }

    login_header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest",
        "Referer": "https://www.instagram.com/accounts/login/",
        "x-csrftoken": csrf
    }

    session = requests.Session()
    login_response = session.post(login_url, data=payload, headers=login_header)
    json_data = json.loads(login_response.text)

    if json_data["authenticated"]:

        print("login successful")
        cookies = login_response.cookies
        cookie_jar = cookies.get_dict()
        csrf_token = cookie_jar['csrftoken']
        print("csrf_token: ", csrf_token)
        session_id = cookie_jar['sessionid']
        print("session_id: ", session_id)

        session.headers.update({'X-CSRFToken': login_response.cookies['csrftoken']})

        r = session.get('https://www.instagram.com/pevitt/')
        print(r.status_code)

        response = r.text
        print(response)
        keywords = ['Fullstack', 'aficionado', 'ajiaco']
        # for item in keywords:
        #     print(item)
        #     print(response.find(item))

        result = [item for item in keywords if response.find(item) > 0]
        print(result)
        if len(result):
            print("Approve")
        else:
            print("Rejected")

    else:
        print("login failed ", login_response.text)

def run():
    authenticate()


if __name__ == '__main__':
    run()
