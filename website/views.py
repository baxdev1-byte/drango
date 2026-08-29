
from django.shortcuts import render
from django.contrib import messages
from website.forms import ContactForm


def home(request):
    return render(request, 'website/home.html')

def about(request):
    return render(request, 'website/about.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for contacting us.')
        else:
            messages.error(request, 'Please correct the error below.')

    else:
        form = ContactForm()
    return render(request, 'website/contact.html', {'form':form})