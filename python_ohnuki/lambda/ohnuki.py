import json
import requests
import datetime
import boto3

s3 = boto3.resource('s3')
bucket = s3.Bucket('unko-sample')
    
def lambda_handler(event, context):
    print('unko')
    # data = get_internet()
    # upload_test(data)
    compare_file()

def get_internet():
    url = "http://michaelsan.livedoor.biz/"
    # urlに対してgetリクエストを投げる
    response = requests.get(url)
    html = response.text
    return html

def upload_test(data):
    now = datetime.datetime.now().strftime('%Y%m%d %H:%M:%S')
    print(now)
    
    # tmpを入れないとエラー
    file = open('/tmp/' + now + '.txt', 'w')
    file.write(data)
    file.close()
    
    bucket.upload_file('/tmp/' + now + '.txt', 'test/' + now + '.txt')
    
def compare_file():
    print('hoge')
    objects_iter = bucket.objects.all()
    print(objects_iter)
    # for object in objects_iter:
        