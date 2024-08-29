from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from .models import data

# Create your views here.


def index(request):
    name='John'
    return render(request,'index.html', {'name': name})

def birth_year(request):
    details = data.objects.all()
   
    age = details[0].age   
    year_of_birth = datetime.today().year - age
    context = {'year': year_of_birth,
              "data": details[0] }
    return render(request,'birth-year.html',context)

def register(request):
    return render(request,'register.html')