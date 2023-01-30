from django.shortcuts import render
from.models import Emp
def home(request):
    e=Emp.objects.all()
    return render(request,'emp/home.html',{'e':e})
# Create your views here.
