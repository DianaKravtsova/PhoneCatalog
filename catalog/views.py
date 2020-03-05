from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import  render

from .models import Catalog

def catalog(request):
    query = Catalog.objects.all()
    phCat = {'context':query}
    return render(request,'index.html',phCat)


# Create your views here.
