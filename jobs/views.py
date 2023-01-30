from django.shortcuts import render

# Create your views here.
from.models import jobs
def home(request):
    j= jobs.objects.all()
    return render(request,'jobs/home.html',{'j':j})

