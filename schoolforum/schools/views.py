from django.shortcuts import render

from .models import School


def home(request):
	schools = School.objects.all()
	return render(request, "schools/home.html", {"schools": schools})