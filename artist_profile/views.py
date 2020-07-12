from django.shortcuts import render
from .models import *

# Create your views here.

def artist_directory(request):
    artist_dir = Artist_dir.objects.all()
    title = "Directory"
    context = { "artist_dir": artist_dir, "title":title}
    return render(request,'artist_profile/art_dir.htm',context)

def artist_profile(request,pk):
    art_prof = Artist_profile.objects.get(id=pk)
    title = "Profile"
    context = {"art_prof": art_prof, "title" : title}
    return render(request,'artist_profile/art_profile.htm',context)