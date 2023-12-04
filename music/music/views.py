from django.shortcuts import render
from MusicBeats.models import Song
# Create your views here.
def index(request):
    song=Song.objects.all()
    return render(request,'index.html',{'song':song})


    