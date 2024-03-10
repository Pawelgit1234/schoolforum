from django.shortcuts import render


def home(request):
	return render(request, "schools/home.html")