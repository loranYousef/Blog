
from django.shortcuts import render
from .models import Post
from .forms import PostForm, KontakttForm


# Create your views here.

def post_list(request):
    all = Post.objects.all()
    return render(request,'post_list.html',{'data':all})
    




def post_detail(request,id):
    post = Post.objects.get(id=id)
    return render(request,'single.html',{'data':post})



# def post_create(request):
#     if request.method =='POST':
#         form = PostForm(request.POST,request.FILES)
#         if form.is_valid():
#             myform= form.save(commit=False)
#             myform.author = request.user
#             myform.save()
#     else:
#         form =PostForm()
#     return render(request,'create.html',{'form':form})

def post_create(request):
    if request.method =='POST':
        form = KontakttForm(request.POST)
        if form.is_valid():
            myform= form.save(commit=False)
            myform.author = request.user
            myform.save()
    else:
        form =KontakttForm()
    return render(request,'form.html',{'form':form})



def edit_post(request,id):
    post =Post.objects.get(id=id)
    if request.method =='POST':
        
        form = PostForm(request.POST,request.FILES, instance =post)
        if form.is_valid():
            myform= form.save(commit=False)
            myform.author = request.user
            myform.save()
    else:
        
        form =PostForm(instance = post)
    return render(request,'edit.html',{'form':form})





def delete_post(request,id):
    post = Post.objects.get(id=id)
    post.delete()
    return redirect('/blog')
    



