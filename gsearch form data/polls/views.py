from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from googlesearch import search
def index(request):
    return HttpResponse("Hello, world!")


from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from datetime import datetime

from .models import Person
from .forms import SubscribeForm

def index(request):
    return HttpResponse("Hello, world!")



def getting(request):
    books = Person.objects.all()
    return render(request, 'get.html', {'books': books})


def home(request):
  # if this is a POST request we need to process the form data
  if request.method == 'POST':
    title = request.POST.get('name')
    website = request.POST.get('web')
    #print(title)
    #print(website)
    try:
        from googlesearch import search
    except ImportError:
        print("No module named 'google' found")
    #website = # need a exact site name including /
    # to search
    query = title#"geeksforgeeks" # keyword
    #rank, rank_list = 1, ""
    squares = []
    for j in search(query, tld="co.in", num=10, stop=10, pause=2):
        #print(j)
        squares.append(j)
    #print(squares)
# app.py

#streaming = ['netflix', 'hulu', 'disney+', 'appletv+']
    streaming = squares
    index = streaming.index(website)
    ranking = index+1
    rankings = "Google rank of your site is:"+str(ranking) #index+1)
    #form = MyForm(request.POST)
    # create a form instance and populate it with data from the request:
    form = SubscribeForm(request.POST)
    # check whether it's valid:
    if form.is_valid():
        name = form.cleaned_data['name']
        web = form.cleaned_data['web']
        p = Person(name=name, web=web, output=ranking, date_subscribed=datetime.now())
        p.save()
        # process the data in form.cleaned_data as required
        
        # redirect to a new URL:
        return render(request, 'puts.html', {'ranking': rankings})
  # if a GET (or any other method) we'll create a blank form    
  else: 
    form = SubscribeForm()

  return render(request, 'index.html', {'form': form})


def variable(request):
    #testvar = 'value'
    testvar = Person.objects.all()
    #rank = MyModel.objects.latest('name')
    #print(rank)
    #rank = MyModel.objects.last()
    #rank = MyModel.objects.filter(name='byjus').last()
    #rank = MyModel.objects.latest('id')
    #rank = list(MyModel.objects.all())[-1]
    rank = Person.objects.latest('id')
    print(rank)
    return render(request, 'i.html', {'testvar': testvar, 'rank': rank})

