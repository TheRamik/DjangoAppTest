from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse

from .models import QuestPin
# Create your views here.

def index(request):
    quest_pin_list = get_list_or_404(QuestPin)
    context = {'quest_pin_list': quest_pin_list}
    return render(request, 'questplugger/index.html', context)
    #return HttpResponse("Hello, world. You're at the questplugger index.")

def detail(request, questpin_id):
    #return HttpResponse("You're looking at question %s." % question_id)
    questpin = get_object_or_404(QuestPin, pk=questpin_id)
    return render(request, 'questplugger/detail.html', {'questpin': questpin})