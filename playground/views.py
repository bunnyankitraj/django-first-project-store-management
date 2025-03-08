from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def calculate():
    return 1 + 1


def say_hello(request):
    x = calculate()
    print(x)
    return render(request, 'hello.html', {'name': 'ankit'})