from django.shortcuts import render
from .models import About , Skills

# Create your views here.

def home(request):
    about = About.objects.last()
    coding_skills = Skills.objects.filter(type='Coding')
    design_skills = Skills.objects.filter(type='Design')
    return render(request,'home.html',{
        'about':about ,
        'coding_skills':coding_skills ,
        'design_skills':design_skills,
        
        })