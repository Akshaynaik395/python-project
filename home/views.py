from django.shortcuts import render

# Create your views here.
from.models import home
def mhome(request):
    return render(request,'home/mhome.html')