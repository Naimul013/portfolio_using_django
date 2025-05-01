from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'portfolio_app/index.html')

def projects(request):
    return render(request,'portfolio_app/projects.html')

def resume(request):
    return render(request,'portfolio_app/resume.html')

def contact(request):
    return render(request,'portfolio_app/contact.html')