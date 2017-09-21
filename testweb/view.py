from django.http import HttpResponse
from django.shortcuts import render

#def hello(request):
#    print request
#    return HttpResponse("Hello world ! ")

def hello(request):
    context          = {}
    context['hello'] = 'Hello World!'
    context['study'] = 'study hard!'
    return render(request, 'hello.html', context)
