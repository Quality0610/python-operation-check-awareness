import json
import requests
from bs4 import BeautifulSoup

import boto3

s3 = boto3.resource('s3')

def lambda_handler(event, context):
    get_internet()
    }


def get_internet():
    // 後で考える
    url = "www.xxxyyyzzz.com"
    response = requests.get(url)
    print(response)
    html = response.text
    print(html)
    soup = BeautifulSoup(html, 'html.parser')

