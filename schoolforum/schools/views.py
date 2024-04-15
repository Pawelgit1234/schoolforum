from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse

from .models import School


def home(request):
	schools = School.objects.all()[:10]
	return render(request, "schools/home.html", {"schools": schools})


def load_more_schools(request):
	try:
		offset = int(request.GET.get('offset', 0))
	except ValueError:
		offset = 0
	schools = School.objects.all()[offset:offset+10]

	serialized_schools = []
	for school in schools:
		image_url = school.photos.first().image.url if school.photos.exists() else None

		serialized_school = {
			'image_url': image_url,
			'name': school.name,
			'description': school.description,
			'slug': school.slug,
		}
		serialized_schools.append(serialized_school)

	return JsonResponse(serialized_schools, safe=False)


def school(request, slug):
	school = get_object_or_404(School, slug=slug)
	return render(request, "schools/school.html", {"school": school})