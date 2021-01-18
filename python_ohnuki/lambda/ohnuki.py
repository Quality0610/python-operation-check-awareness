import json
import requests
from bs4 import BeautifulSoup

import boto3

s3 = boto3.resource('s3')
    
def lambda_handler(event, context):
    get_internet()
    # file = get_internet()
    # print('unko')
    # upload_test(file)
    
def get_internet():
    url = "https://www.yahoo.co.jp/"
    # yahooに対してgetリクエストを投げる
    response = requests.get(url)
    print(response)
    html = response.text
    print(html)
    soup = BeautifulSoup(html, 'html.parser')
    return soup

def upload_test(file):
    bucket = s3.Bucket('unko-sample')
    bucket.upload_file('sample.html', file)
