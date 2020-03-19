from django.shortcuts import render
from tv.models import channel

# Create your views here.
def live(request):
    return render(request,'live.html')

def index(request):
    channels = channel.objects.all()
    return render(request,'index.html',{'channels':channels})