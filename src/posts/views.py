from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def post_create(request):
    return HttpResponse("<h1>create</h1>")

def post_detail(request):# retrieve
    return render(request, "index.html")

def post_list(request):# list item
    return HttpResponse("<h1>list</h1>")

def post_update(request):
    return HttpResponse("<h1>Hello</h1>")

def post_delete(request):
    return HttpResponse("<h1>Hello</h1>")
