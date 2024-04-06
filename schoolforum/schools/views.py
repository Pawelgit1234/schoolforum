from django.shortcuts import render, get_object_or_404

from .models import School


def home(request):
	schools = School.objects.all()
	return render(request, "schools/home.html", {"schools": schools})


def school(request, slug):
	school = get_object_or_404(School, slug=slug)
	return render(request, "schools/school.html", {"school": school})