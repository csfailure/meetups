from django.shortcuts import render, redirect
from .forms import RegistrationForm

from .models import Meetup, Participant

# Create your views here.

def index(request):
    meetups = Meetup.objects.all()
    return render(request, 'meetups/index.html',{
        'show_meetups': True,
        'meetups': meetups
        })

def details(request, meetup_slug):
    try:
        selected_meetup = Meetup.objects.get(slug=meetup_slug)
        if request.method == 'GET':
            reg_form = RegistrationForm()
        
        else:
            reg_form = RegistrationForm(request.POST)
            if reg_form.is_valid():
                useremail = reg_form.cleaned_data['email']
                participant, _ =  Participant.objects.get_or_create(email=useremail)      
                selected_meetup.participant.add(participant)  
                return redirect('confirmreg', meetup_slug=meetup_slug)
        
        return render(request, 'meetups/details.html', {
                    'meetup_found': True,
                    'meetup': selected_meetup,
                    'form': reg_form
                })

    except Exception as exc:
        return render(request, 'meetups/details.html', {
            'meetup_found': False
        })

def confirmed(request, meetup_slug):
    meetup = Meetup.objects.get(slug = meetup_slug)
    return render(request, 'meetups/confirmed.html', {
        'organizer_email': meetup.organizer_email
    })