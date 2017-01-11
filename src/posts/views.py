from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Post

def post_create(request):
    return HttpResponse("<h1>create</h1>")

def post_detail(request):# retrieve
    # instance = Post.objects.get(id=2)
    instance = get_object_or_404(Post, id="3")
    context = {
        'instance': instance,
        'title': instance.title,
    }
    return render(request, "post_detail.html", context)

def post_list(request):# list item
    # if request.user.is_authenticated():
    queryset = Post.objects.all()
    context = {
        'object_list': queryset,
        'title': "List",
    }
    return render(request, "index.html", context)
    # else:
    #     return HttpResponse("<h1>Hell No!!</h1>")

def post_update(request):
    return HttpResponse("<h1>Hello</h1>")

def post_delete(request):
    return HttpResponse("<h1>Hello</h1>")
