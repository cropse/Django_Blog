from django.shortcuts import render, get_object_or_404, redirect
from .models import Introduce

# Create your views here.
def soundcloud(request):
    return render(request, "soundcloud/soundcloud.html")

def about_me(request):
    query_set = Introduce.objects.first()
    # print(query_set.content)
    # print(query_set.get_markdown())
    context={
        'Introduce': query_set,
    }
    return render(request, "about_me/about_me.html", context)
