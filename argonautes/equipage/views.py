from django.shortcuts import render
from .models import Crew_member

def crew(request):
    members = Crew_member.objects.filter(belong_crew=True).order_by('created_date')
    return render(request, 'equipage/index.html', {'members' : members})
