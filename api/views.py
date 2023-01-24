from django.http import HttpResponse
from django.shortcuts import render

def add(request):
  return HttpResponse('Add')

def divide(request):
  return HttpResponse('Divide')

def multiply(request):
  return HttpResponse('Multiply')

def random_string(request):
  return HttpResponse('Random String')

def square_root(request):
  return HttpResponse('Square Root')

def subtract(request):
  return HttpResponse('Subtract')

