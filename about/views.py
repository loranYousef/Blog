from django.shortcuts import render
from .models import About , Skills , Educations ,Experience , Service, Projects
from posts.models import Post
from posts.forms import PostForm

# Create your views here.

def home(request):
    about = About.objects.last()
    coding_skills = Skills.objects.filter(type='Coding')
    design_skills = Skills.objects.filter(type='Design')
    education = Educations.objects.all()
    experience = Experience.objects.all()
    service = Service.objects.all()
    projects = Projects.objects.all()
    posts = Post.objects.all()[:3]
    return render(request,'home.html',{
        'about':about ,
        'coding_skills':coding_skills ,
        'design_skills':design_skills,
        'education' : education,
        'experience': experience,
        'service' : service,
        'projects': projects,
        'posts' : posts,


        
        })

def post_create(request):
        if request.method =='POST':
            form = PostForm(request.POST,request.FILES)
            if form.is_valid():
                myform= form.save(commit=False)
                myform.author = request.user
                myform.save()
        else:
            form =PostForm()
        return render(request,'home.html',{'form':form})
