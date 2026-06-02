from django.shortcuts import render
from trainers.models import Trainer
from trainings.models import Service
from directors.models import Director

# Create your views here.

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def contact(request):
    return render(request, 'contact.html')

def trainers(request):

    trainers_data = Trainer.objects.all()

    context = {
        'trainers_data': trainers_data
    }

    return render(request, 'trainers.html', context)

def services(request):

    services_data = Service.objects.all()

    context = {
        'services_data': services_data
    }

    return render(request, 'services.html', context)

def home(request):

    directors = Director.objects.all()

    context = {
        'directors': directors
    }

    return render(request, 'index.html', context)

