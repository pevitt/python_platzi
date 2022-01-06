import random
import os
import requests


def run():
    print("Hola")
    r = requests.get('https://es-la.facebook.com/venta.zapatos.5220')
    print(r.status_code)

    response = r.text
    #print(response)
    keywords = ['Zapatos', 'envio', 'body', 'feed']
    # for item in keywords:
    #     print(item)
    #     print(response.find(item))

    result = [item for item in keywords if response.find(item) > 0]
    print(result)
    if len(result):
        print("Approve")
    else:
        print("Rejected")


if __name__ == '__main__':
    run()
