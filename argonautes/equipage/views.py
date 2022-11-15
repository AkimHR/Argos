from django.shortcuts import render, redirect
from .models import Crew_member
from .formulaire import CrewForm

def crew(request):
    
    if request.method == 'POST':
        form = CrewForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    else:
        form = CrewForm()
        
    members = Crew_member.objects.filter(belong_crew=True).order_by('created_date')

    return render(request, 'equipage/index.html', {'form' : form, 'members' : members})
        