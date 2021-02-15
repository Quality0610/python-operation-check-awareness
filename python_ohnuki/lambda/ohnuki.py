import json
import requests
import datetime
import boto3

s3 = boto3.resource('s3')
bucket = s3.Bucket('unko-sample')
bucket_name = 'unko-sample'
key = "test/"
target_url = ''
webhook_url = ''
    
def lambda_handler(event, context):
    data = get_internet()
    upload_bucket(data)
    compare_file_and_notice()

def get_internet():
    response = requests.get(target_url)
    html = response.text
    return html

def upload_bucket(data):
    now = datetime.datetime.now().strftime('%Y%m%d %H:%M:%S')
    
    # tmpを入れないとエラー
    file = open('/tmp/' + now, 'w')
    file.write(data)
    file.close()
    
    bucket.upload_file('/tmp/' + now, key + now)
    
def compare_file_and_notice():

    objs = bucket.meta.client.list_objects_v2(
        Bucket = bucket_name,
        Prefix = key
    )

    obj_list = []
    tmp_dictionary_1 = {}
    tmp_dictionary_2 = {}
    tmp = {}
    loop_first_f = True
    loop_second_f = True
    
    # 更新時刻が最新のオブジェクト2つをobj_listに入れる
    for o in objs.get('Contents'):
        
        if loop_first_f:
            tmp_dictionary_1 = {
                "key": o.get('Key'),
                "last_modified": o.get('LastModified')
            }
            loop_first_f = False
        
        elif loop_second_f:
            tmp_dictionary_2 = {
                "key": o.get('Key'),
                "last_modified": o.get('LastModified')
            }
            loop_second_f = False
            
        else:
            if tmp_dictionary_1["last_modified"] >= tmp_dictionary_2["last_modified"]:
                tmp = {
                    "key": tmp_dictionary_1["key"],
                    "last_modified": tmp_dictionary_1["last_modified"]
                } 
                
                tmp_dictionary_1["key"] = tmp_dictionary_2["key"]
                tmp_dictionary_1["last_modified"] = tmp_dictionary_2["last_modified"]
                tmp_dictionary_2["key"] = tmp["key"]
                tmp_dictionary_2["last_modified"] = tmp["last_modified"]
                
            if tmp_dictionary_1["last_modified"] <= o.get('LastModified'):
                tmp_dictionary_1["key"] = o.get('Key')
                tmp_dictionary_1["last_modified"] = o.get('LastModified')
    
    latest_s3_obj_1 = get_s3file(tmp_dictionary_1["key"])
    latest_s3_obj_2 = get_s3file(tmp_dictionary_1["key"])
        
    if latest_s3_obj_1 != latest_s3_obj_2:
        notice_slack()

def get_s3file(file_name):

    s3_client = boto3.client('s3')
    response = s3_client.get_object(Bucket=bucket_name, Key=file_name)
    return response['Body'].read().decode('utf-8')
    
def notice_slack():
    text = "更新されましたよ"
    
    requests.post(webhook_url, data = json.dumps({
        "text": text
    }))    