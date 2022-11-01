from django.shortcuts import render
from django.http import HttpResponse,HttpRequest

def counters(request):
    return render(request,'index.html')
    
