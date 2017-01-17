from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
from .models import Post
from .forms import PostForm

def post_create(request):
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        print(form.cleaned_data.get("title"))
        instance = form.save(commit=False)
        instance.save()
        # message success
        messages.success(request, "Successfully Create")
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "form": form,
    }
    return render(request, "post_form.html", context)
 
def post_detail(request, id=None):# retrieve
    instance = get_object_or_404(Post, id=id)
    context = {
        'instance': instance,
        'title': instance.title,
    }
    return render(request, "post_detail.html", context)

def post_list(request):# list item
    queryset_list = Post.objects.all()
    paginator = Paginator(queryset_list, 6) # Show 25 contacts per page
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)

    context = {
        'object_list': queryset,
        'title': "List",
        'page_request_var': page_request_var,
    }
    return render(request, "post_list.html", context)




def post_update(request, id=None):
    instance = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, request.FILES or None, instance=instance)
    # form is posted
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "<a href='#'>Item</a> Edit", extra_tags="html-safe")
        return HttpResponseRedirect(instance.get_absolute_url())
    # load old instance
    context = {
        'instance': instance,
        'title': instance.title,
        'form':form,
    }
    return render(request, "post_form.html", context)

def post_delete(request, id=None):
    instance = get_object_or_404(Post, id=id)
    instance.delete()
    messages.success(request, "Successfully Delete")
    return redirect("posts:list")
