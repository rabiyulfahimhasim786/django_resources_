from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse

import os
def index(request):
    return HttpResponse("Hello, world!")

from .models import Document
def home(request):
    documents = Document.objects.all()
    rank = Document.objects.latest('id')
    print(rank)
    return render(request, 'home.html', { 'documents': documents })


from django.shortcuts import render
from django.shortcuts import render
from mysite import settings
from django.core.files.storage import FileSystemStorage

def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        print(uploaded_file_url)
        return render(request, 'simple_upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'simple_upload.html')

from .forms import DocumentForm
def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            #func_obj = form
            #func_obj.sourceFile = form.cleaned_data['sourceFile']
            form.save()
            #print(form.Document.document)
            #form.save()
            return redirect('home')
    else:
        form = DocumentForm()
    return render(request, 'model_form_upload.html', {
        'form': form
    })