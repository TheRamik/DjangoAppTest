# quests/views.py
from django.shortcuts import render
from django.http import HttpResponse
from .forms import QuestSubmissionForm
# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the quest index. There will be a quest list here in the future.")

def quest_form(request):
    if request.method == 'GET':
        form = QuestSubmissionForm()
    else:
        form = QuestSubmissionForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            rank = form.cleaned_data['rank']
            roles = form.cleaned_data['roles']
            team_size = form.cleaned_data['team_size']
            duration = form.cleaned_data['duration']
            form.save()
            messages.info(request, 'Your message has been sent successfully!')
            return HttpResponseRedirect('/')
    return render(request, "questform.html", {'form': form})