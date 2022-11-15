from django import forms

from .models import Crew_member

class CrewForm(forms.ModelForm):

    class Meta:
        model = Crew_member
        fields = ( 'name',)