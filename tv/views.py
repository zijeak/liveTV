from django.shortcuts import render
from tv.models import channel,Category,Notice

# Create your views here.
def live(request):
    return render(request,'live.html')

def index(request,id):
    if(id==''):
        channels = channel.objects.all()
    else:
        channels = channel.objects.filter(category__id = id)
    categorys = Category.objects.all()
    notices = Notice.objects.all()
    notice = Notice.objects.order_by('-id')[:1][0]
    print(notice)
    return render(request,'index.html',{'channels':channels,'categorys':categorys,'notice':notice})

def ys(request):
    channels = channel.objects.filter(category__name = '央视频道')
    categorys = Category.objects.all()

    return render(request,'index.html',{'channels':channels,'categorys':categorys})