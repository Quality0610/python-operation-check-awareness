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
    objs = bucket.meta.client.list_objects_v2(
        Bucket='unko-sample',
        Prefix='test/'
    )

    obj_list = []
    tmp_dictionary_1 = {}
    tmp_dictionary_2 = {}
    loop_first_f = True
    loop_second_f = True
    
    # 更新時刻が最新のオブジェクト2つをobj_listに入れる
    for o in objs.get('Contents'):
        print(o.get('Key'))
        print(o.get('LastModified'))
        
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
            if tmp_dictionary_1["last_modified"] <= o.get('LastModified'):
                tmp_dictionary_1["key"] = o.get('Key')    
                tmp_dictionary_1["last_modified"] = o.get('LastModified')
              
            elif tmp_dictionary_2["last_modified"] <= o.get('LastModified'):
                tmp_dictionary_2["key"] = o.get('Key')    
                tmp_dictionary_2["last_modified"] = o.get('LastModified')
            
    obj_list.append(tmp_dictionary_1)
    obj_list.append(tmp_dictionary_2)

    print('--------------------------------------------')        
    print(obj_list)
    
    for obj in obj_list:
        print('!!------------------------------------------')        
        print(obj["key"])
        print(obj["last_modified"])
    
    obj_list[0].["key"] 
          
# def notice_slack:
    