from django.shortcuts import render
from .models import Post
from .forms import PostForm

# Create your views here.

def post_list(request):
    all = Post.objects.all()
    return render(request,'posts.html',{'data':all})




def post_detail(request,id):
    post = Post.objects.get(id=id)
    return render(request,'single.html',{'data':post})

def create_post(request):
    if request.method =='POST':
        form =PostForm(request.POST,request.Files)
        if form.is_valid():
            form.save()
    else:
        form = PostForm()

    return render(request,'create.html',{'form':form})
    

def edit_post(request,id):
    post = Post.objects.get(id=id)
    if request.method =='POST':
        form =PostForm(request.POST,request.Files)
        if form.is_valid():
            myform = form.save(commit = False)
            myform.author = request.user

    else:
        form = PostForm()

    return render(request,'edit.html',{'form':form})
    








def delete_post():
    pass