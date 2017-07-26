from django.http import HttpResponse
from django.shortcuts import render
import random
# Create your views here.

def home(request):
    #return HttpResponse("helloddsdf")
    num = random.randint(1,20000)
    return render(request,"index.html",{"content": num})