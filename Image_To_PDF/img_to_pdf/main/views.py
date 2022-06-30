from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
import os
from PIL import Image
from time import sleep
# Create your views here.
t=0


def name():
    global t
    t+=1
    return str(t)


def index(request):
    return render(request, 'test.html')


def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        r = dict(request.FILES)
        file = r['myfile']
        print(request.FILES)
        print(r)
        for myfile in file:
            fs = FileSystemStorage()
            filename = fs.save(name() + '.' + myfile.name.split('.')[-1], myfile)
            uploaded_file_url = fs.url(filename)
            # myfile.pop(-1)

        li_files = os.listdir('media')
        img_li = []
        for file in li_files:
            img_li.append(Image.open(os.path.join('media',file)).convert('RGB'))
        img_li[0].save('static\converted_pdf.pdf', save_all=True, append_images=img_li[1:])
        for file in li_files:
            os.remove(os.path.join('media',file))

        return render(request, 'loading_page.html')
    # error page.....
    return render(request, 'loading_page.html')


