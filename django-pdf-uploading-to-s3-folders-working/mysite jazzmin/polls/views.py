#from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework.response import Response
from .serializers import DropboxSerializer#, StandardsSerializer, CountriesSerializer, TagSerializer

from .models import Dropbox#, Standards, Countries, Tag
# Create your views here.
from django.http import Http404
from rest_framework.views import APIView
from rest_framework import status
# Create your views here.
from django.http import HttpResponse

#AWS s3
import boto3
import os
from functools import reduce
#import boto3
ACCESS_KEY = "ACCESS_KEY"
SECRET_KEY = "SECRET_KEY"

from functools import reduce

def index(request):
    return HttpResponse("Hello, world.")

def some_views(request):
    return JsonResponse({"key": "value"})

def download_dir(request):
    s3_client = boto3.client('s3', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)
    response = s3_client.list_objects_v2(Bucket='s3bucketname', Prefix='table')
    all = response['Contents']        
    latest = max(all, key=lambda x: x['LastModified'])
    print(latest)
        #print(latest.values())
    list(reduce(lambda x, y: x + y, latest.items()))
    b = list(reduce(lambda x, y: x + y, latest.items()))
    print(b[1])

        #file downloading 
        #print(latest.values())
    list(reduce(lambda x, y: x + y, latest.items()))
    bb = list(reduce(lambda x, y: x + y, latest.items()))
        #print(a[1])
    urllinks = bb[1]
    data = urllinks[0:71]
    prefix = data
    local = 'localfoldername'
    bucket = 's3bucketname'
    client=s3_client
    keys = []
    dirs = []
    next_token = ''
    base_kwargs = {
        'Bucket':bucket,
        'Prefix':prefix,
    }
    while next_token is not None:
        kwargs = base_kwargs.copy()
        if next_token != '':
            kwargs.update({'ContinuationToken': next_token})
        results = client.list_objects_v2(**kwargs)
        contents = results.get('Contents')
        for i in contents:
            k = i.get('Key')
            if k[-1] != '/':
                keys.append(k)
            else:
                dirs.append(k)
        next_token = results.get('NextContinuationToken')
    for d in dirs:
        dest_pathname = os.path.join(local, d)
        if not os.path.exists(os.path.dirname(dest_pathname)):
            os.makedirs(os.path.dirname(dest_pathname))
    for k in keys:
        dest_pathname = os.path.join(local, k)
        if not os.path.exists(os.path.dirname(dest_pathname)):
            os.makedirs(os.path.dirname(dest_pathname))
        client.download_file(bucket, k, dest_pathname)
    #download_dir(urllinks[0:71], 'localfoldername', 's3bucketname', client=s3_client)
    #return HttpResponse("Hello world")
    return JsonResponse({"key": data})
    #download_dir('s3foldername', 'localfoldername', 's3bucketname', client=s3_client)
  
def bot_views(request):


    ACCESS_KEY = "ACCESS_KEY"
    SECRET_KEY = "SECRET_KEY"
    s3_client = boto3.client('s3', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)
    response = s3_client.list_objects_v2(Bucket='s3bucketname', Prefix='s3foldername')
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
    #https://s3bucketname.s3.amazonaws.com/json/data.json
    url = f"https://s3bucketname.s3.amazonaws.com/{urllink}"
    print(url)
    datas = {"key": url}
    return JsonResponse({"code": "1", "status": "200", "data": [datas]})


def botkv_views(request):
    ACCESS_KEY = "ACCESS_KEY"
    SECRET_KEY = "SECRET_KEY"
    s3_client = boto3.client('s3', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)
    response = s3_client.list_objects_v2(Bucket='s3bucketname', Prefix='s3foldername')
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
    #https://s3bucketname.s3.amazonaws.com/json/data.json
    url = f"https://s3bucketname.s3.amazonaws.com/{urllink}"
    print(url)
    datas = {"key": url}
    return JsonResponse({"code": "1", "status": "200", "data": [datas]})


class DropboxList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        dropbox = Dropbox.objects.all()
        serializer = DropboxSerializer(dropbox, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = DropboxSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DropboxDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Dropbox.objects.get(pk=pk)
        except Dropbox.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        dropbox = self.get_object(pk)
        serializer = DropboxSerializer(dropbox)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        dropbox = self.get_object(pk)
        serializer = DropboxSerializer(dropbox, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)