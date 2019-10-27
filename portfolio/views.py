from django.shortcuts import render
from .models import Project
# Create your views here.
def suitcase(request):
    projects = Project.objects.all()
    # Diccionario de contexto
    return render(request,"portfolio/suitcase.html",{'projects':projects})
