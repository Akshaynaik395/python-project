from django.shortcuts import render, get_object_or_404
from.models import Blogs
# Create your views here.
def bhome(request):
    b=Blogs.objects.all()
    return render(request,'blogs/bhome.html',{'b':b})

def detail(request,blog_id):
    blogdetail= get_object_or_404(Blogs,pk=blog_id)
    return render(request,'blogs/detail.html',{'blog':blogdetail})