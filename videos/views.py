from django.shortcuts import render
from .forms import Video_Form
from .models import Video
from django.http import JsonResponse
# Create your views here.
def home_view(request):
    return render(request,'pages/home.html',{})


def video_create_view(request):
    form = Video_Form(request.POST or None)
    print(request.is_ajax())
    if form.is_valid():
        form.save()
        form = Video_Form()

    return render(request, 'videos/video_create.html', {"form": form})

def video_json_view(request):
    qs = Video.objects.all()
    
    video_list = [{"link": x.link, "title": x.title} for x in qs]

    data = {
        "response": video_list
        
    }
    return JsonResponse(data)