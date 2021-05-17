import json
import requests


def run():
    url = 'https://covid-193.p.rapidapi.com/statistics'
    headers = {
        'x-rapidapi-key': '1fed9db1c3msh01d8790115aa542p14fd47jsn5ffe2993cf42',
        'x-rapidapi-host': 'covid-193.p.rapidapi.com',
        'useQueryString': 'true'
    }

    response = requests.get(url, headers=headers)
    dict_date = response.json()
    print(dict_date)


if __name__ == '__main__':
    run()
