from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


# Create your views here.
from django.http import HttpResponse


from django.shortcuts import render
from .models import MyModel
from .forms import MyForm

def index(request):
    return HttpResponse("Hello, world.")

def getting(request):
    books = MyModel.objects.all()
    return render(request, 'get.html', {'books': books})

def my_form(request):
  if request.method == "POST":
    title = request.POST.get('name')
    website = request.POST.get('web')
    print(title)
    print(website)
    form = MyForm(request.POST)
    if form.is_valid():
      form.save()
  else:
      form = MyForm()
  return render(request, 'index.html', {'form': form})

#def saveCriteria(request):
 ##   context = {}
 #   if request.method == "POST":
 #       title = request.POST.get('quantity')
 #       print(title)
 #   return render(request, "home.html", context)