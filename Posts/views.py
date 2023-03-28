from django.shortcuts import render
from .models import Post

# Create your views here.

def post_list(request):
    all = Post.objects.all()
    return render(request,'posts.html',{'data':all})




def post_detail(request):
    pass