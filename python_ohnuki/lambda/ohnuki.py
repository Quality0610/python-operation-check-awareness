import json
import requests
from bs4 import BeautifulSoup

def lambda_handler(event, context):
    get_internet()


    }


def get_internet():
    url = "www.xxxyyyzzz.com"
    response = requests.get(url)
    print(response)
    html = response.text
    print(html)
    soup = BeautifulSoup(html, 'html.parser')