from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the forms index.")

def get_contact(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            cc_myself = form.cleaned_data['cc_myself']

            print("subject: {}, message: {}, sender: {}".format(subject, message, sender))
            recipients = ['rickytham123@gmail.com']
            if cc_myself:
                recipients.append(sender)
            send_mail(subject, message, sender, recipients)
            return HttpResponseRedirect('success')
    
    return render(request, 'contact.html', {'form': form})

def successView(request):
    return HttpResponse('Success! Thank you for your message.')