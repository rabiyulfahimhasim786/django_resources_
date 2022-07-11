from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

#from django.utils import simplejson
from django.http import JsonResponse

from functools import reduce
import boto3

def some_views(request):
    return JsonResponse({"key": "value"})
    
def index(request):
    return HttpResponse("Hello, world.")

def bot_views(request):
    ACCESS_KEY = "ACCESS_KEY"
    SECRET_KEY = "SECRET_KEY"

    s3_client = boto3.client('s3', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)
    response = s3_client.list_objects_v2(Bucket='bucket_name', Prefix='foldername')
    all = response['Contents']        
    latest = max(all, key=lambda x: x['LastModified'])
    print(latest)
    #print(latest.values())
    list(reduce(lambda x, y: x + y, latest.items()))
    a = list(reduce(lambda x, y: x + y, latest.items()))
    print(a[1])

    #file downloading 
    #print(latest.values())
    list(reduce(lambda x, y: x + y, latest.items()))
    a = list(reduce(lambda x, y: x + y, latest.items()))
    #print(a[1])
    urllink = a[1]
    #https://bucket_name.amazonaws.com/json/data.json
    url = f"https://bucket_name.s3.amazonaws.com/{urllink}"
    print(url)
    datas = {"key": url}
    return JsonResponse({"code": "1", "status": "200", "data": [datas]})


def botkv_views(request):
    ACCESS_KEY = "ACCESS_KEY"
    SECRET_KEY = "SECRET_KEY"

    s3_client = boto3.client('s3', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)
    response = s3_client.list_objects_v2(Bucket='bucket_name', Prefix='foldername')
    all = response['Contents']        
    latest = max(all, key=lambda x: x['LastModified'])
    print(latest)
    #print(latest.values())
    list(reduce(lambda x, y: x + y, latest.items()))
    a = list(reduce(lambda x, y: x + y, latest.items()))
    print(a[1])

    #file downloading 
    #print(latest.values())
    list(reduce(lambda x, y: x + y, latest.items()))
    a = list(reduce(lambda x, y: x + y, latest.items()))
    #print(a[1])
    urllink = a[1]
    #https://ocr-textract-key-value-output.s3.amazonaws.com/json/data.json
    url = f"https://bucket_name.s3.amazonaws.com/{urllink}"
    print(url)
    datas = {"key": url}
    return JsonResponse({"code": "1", "status": "200", "data": [datas]})


