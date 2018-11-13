from django.shortcuts import render
from about.models import Project

def splash(request):
    return render(request, 'splash.html')

def projects(request):
    projects = Project.objects.all()
    return render(request, 'projects.html', {'projects': projects})

def research(request):
    return render(request, 'research.html')

def consulting(request):
    return render(request, 'consulting.html')

def teaching(request):
    return render(request, 'teaching.html')