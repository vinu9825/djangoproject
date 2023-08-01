from django.shortcuts import render
from django.http import HttpResponse
def homepage(request):
    return render(request,'index.html')
def hello(request):
    return HttpResponse('hello its me vinu')
def contact(request):
    return HttpResponse('hello my brother how are you')