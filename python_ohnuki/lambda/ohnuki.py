import json
import requests
# from import BeautifulSoup
import datetime


import boto3

s3 = boto3.resource('s3')
    
def lambda_handler(event, context):
    print('unko')
    data = get_internet()
    # print(file)
    upload_test(data)
    # file = get_internet()
    # print('unko')
    # upload_test(file)
    
def get_internet():
    url = "http://michaelsan.livedoor.biz/"
    # urlに対してgetリクエストを投げる
    response = requests.get(url)
    # print(response)
    html = response.text
    return html
    # print(html)
    # soup = BeautifulSoup(html, 'html.parser')
    # return soup

def upload_test(data):
    today = datetime.date.today().strftime('%Y%m%d')
    print(today)
    # tmpを入れないとエラー
    file = open('/tmp/' + today + '.txt', 'w')
    file.write(data)
    file.close()

    # s3 = boto3.resource('s3')
    
    # for bucket in s3.buckets.all():
    #     print(bucket.name)
    bucket = s3.Bucket('unko-sample')
    bucket.upload_file("test/", file)
