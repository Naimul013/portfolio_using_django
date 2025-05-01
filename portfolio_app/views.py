from django.shortcuts import render
from .models import *
# Create your views here.
def index(request):
    return render(request,'portfolio_app/index.html')

def projects(request):
    return render(request,'portfolio_app/projects.html')

def resume(request):
    experiences = Experience.objects.all()
    educations = Education.objects.all()
    ecas = ExtraCurriculum.objects.all()
    skills = ProfessionalSkill.objects.all()
    program_langs = ProgrammingLanguage.objects.all()
    langs = Fluency.objects.all()

    context = {'experiences':experiences, 'educations': educations, 'ecas': ecas, 'skills': skills, 'program_langs': program_langs,
              'langs':langs }
    return render(request,'portfolio_app/resume.html', context)

def contact(request):
    return render(request,'portfolio_app/contact.html')