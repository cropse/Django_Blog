from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def post_create(request):
    return HttpResponse("<h1>create</h1>")

def post_detail(request):# retrieve
    context = {
        'title': "Detail",
    }
    return render(request, "index.html", context)

def post_list(request):# list item
    if request.user.is_authenticated():
        context = {
            'title': "List",
        }
        return render(request, "index.html", context)
    else:
        return HttpResponse("<h1>Hell No!!</h1>")

def post_update(request):
    return HttpResponse("<h1>Hello</h1>")

def post_delete(request):
    return HttpResponse("<h1>Hello</h1>")
