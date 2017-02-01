from django.shortcuts import render, get_object_or_404
from filer.models.filemodels import File, Folder

# Create your views here.
def gallery(request, folder_id=None):

# get_object_or_404

    # gallery_folder_set = Folder.objects.get(name="Gallery").get_children()
    
    # folder_id=6

    if folder_id:
        gallery_set = File.objects.filter(folder_id=folder_id)
    else:
        gallery_set = File.objects.filter(name="Icon")

    context = {
    'gallery_set': gallery_set,
    'is_folder': folder_id,
    }
    return render(request, "gallery/gallery.html", context)


