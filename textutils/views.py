from django.http import HttpResponse
from django.shortcuts import render
from.forms import studentregistration
def index(request):
   return render(request, 'index.html')
    #return HttpResponse('''<h1>Welcome To World</h1> <a href="https://google.co.in">go to our website


def login(request):
    return render(request,'form.html')
def filecomplaint(request):
    return render(request,'filecomplaint.html')
def browsecomplaint(request):
    return render(request,'browsecomplaint.html')