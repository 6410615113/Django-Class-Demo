from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    # return HttpResponse('<h1>Hello, WOrld!</h1>')
    return render(request, 'hello/index.html')

def greet(request, name):
    # return HttpResponse(f'<h1>Hello, {name.title()!</h1>}')
    from django.utils import timezone
    hour = timezone.localtime().hour
    return render(request, 'hello/greet.html', {
        'name': name.title()})