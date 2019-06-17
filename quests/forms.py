from django import forms
from .choices import *
from .models import QuestPin

class QuestSubmissionForm(forms.ModelForm):
    name = forms.CharField()
    rank = forms.ChoiceField(
        choices=RANK_CHOICES, 
    )
    roles = forms.MultipleChoiceField(
        widget=forms.SelectMultiple,
        choices=ROLE_CHOICES
    )
    team_size = forms.ChoiceField(
        choices=TEAM_SZ_CHOICES,
    )
    duration = forms.DurationField()

    class Meta:
        model = QuestPin
        fields = ('name', )