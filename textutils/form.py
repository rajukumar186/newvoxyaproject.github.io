from django.http import HttpResponse
def removepunc(request):
    return HttpResponse('''<a href="#">removepunc</a>''')
def capatilizefirst(request):
    return HttpResponse('''<a href="#">capatilizefirst</a>''')
def spaceremover(request):
    return HttpResponse('''<a href="#">spaceremover</a>''')
def back(request):
    return HttpResponse('''<a href="./views.py">back</a>''')
