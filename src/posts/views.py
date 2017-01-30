from urllib.parse import quote_plus
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils import timezone
from django.db.models import Q

# Create your views here.
from .models import Post
from .forms import PostForm
from zinnia.models import Entry
from zinnia.models import Category
from zinnia.managers import tags_published
# from .models import EntryGallery

# from zinnia.views.search import EntrySearch

def CustomTemplateEntrySearch(request):
    # template_name = 'custom/base.html'
    context = {
        # "form": form,
    }
    return render(request, "zinna/base.html")

def post_create(request):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404

    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        print(form.cleaned_data.get("title"))
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        # message success
        messages.success(request, "Successfully Create")
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "form": form,
    }
    return render(request, "posts/post_form.html", context)
 
def post_detail(request, slug=None):# retrieve
    instance = get_object_or_404(Entry, slug=slug)
    # if instance.draft or instance.publish > timezone.now().date():
    #     if not request.user.is_staff or not request.user.is_superuser:
    #         raise Http404
    share_string = quote_plus(instance.content)
    context = {
        'instance': instance,
        'title': instance.title,
        'share_string': share_string,

    }
    return render(request, "posts/post_detail.html", context)

def post_list(request):# list item
    today = timezone.now().date()

    # print(dir(entries_published))
    # queryset_list = Entry.published.on_site()

    search_list = request.GET.get("user_search")
    if search_list:
        queryset_list = Entry.published.search(search_list)
    elif request.user.is_staff or request.user.is_superuser:
        queryset_list = Entry.published.on_site()
    else:
        queryset_list = Entry.objects.filter(status=2)
        
    queryset = queryset_list
    #     queryset_list = queryset_list.filter(
    #         Q(title__icontains=search_list) |
    #         Q(content__icontains=search_list)|
    #         Q(user__first_name__icontains=search_list)|
    #         Q(user__last_name__icontains=search_list)
    #         )
    print("Tagg")
    # print(Entry.tags.title())

    paginator = Paginator(queryset_list, 5) # Show 5 contacts per page
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
        'entry': Entry,
        'object_list': queryset,
        'title': "Entry_List",
        'page_request_var': page_request_var,
        'today': today,
    }
    return render(request, "posts/post_list.html", context)




def post_update(request, slug=None):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404 
    instance = get_object_or_404(Post, slug=slug)
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
    return render(request, "posts/post_form.html", context)

def post_delete(request, slug=None):
    if request.user.is_staff or not request.user.is_superuser:
        raise Http404    
    instance = get_object_or_404(Post, slug=slug)
    instance.delete()
    messages.success(request, "Successfully Delete")
    return redirect("posts:list")
