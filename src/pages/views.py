from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
def soundcloud(request):
    return render(request, "soundcloud/soundcloud.html")
