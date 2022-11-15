from django.forms import ModelForm

from .models import Crew_member

class CrewForm(ModelForm):

    class Meta:
                
        model = Crew_member
        fields = ['name']