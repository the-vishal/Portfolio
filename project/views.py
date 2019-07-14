from django.shortcuts import render, get_object_or_404
from .models import Project
# Create your views here.

def index(request):
	projects =  Project.objects
	return render(request,"project/index.html", {'projects':projects})


def detail(request, course_id):
	projects =  Project.objects
	return render(request,"project/index.html")