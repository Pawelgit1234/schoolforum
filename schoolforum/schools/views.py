from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_GET

from .models import School, Discussion


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


def load_more_discussions(request, slug):
	try:
		offset = int(request.GET.get('offset', 0))
	except ValueError:
		offset = 0
	school = get_object_or_404(School, slug=slug)

	serialized_discussions = []
	for d in school.school_discussions.all()[offset:offset+10]:
		overall_rating = d.overall_rating_balance()
		comments_count = d.discussion_comments.count()

		serialized_discussion = {
			'user': d.user.username,
			'avatar_url': d.user.profile.avatar.url,
			'creation_date': d.created_at.strftime('%d.%m.%Y %H:%M'),
			'type': d.get_lesson_type_display(),
			'rating': overall_rating,
			'comments_count': comments_count,
			'title': d.title,
			'id': d.id,
		}

		serialized_discussions.append(serialized_discussion)
	return JsonResponse(serialized_discussions, safe=False)


def search(request):
	query = request.GET.get('q')
	schools = School.objects.filter(name__icontains=query)
	discussions = Discussion.objects.filter(title__icontains=query)

	context = {
		'schools': schools,
		'discussions': discussions,
		'query': query,
	}

	return render(request, 'schools/search_results.html', context)


def discussion(request, id):
	dis = get_object_or_404(Discussion, id=id)
	return render(request, "schools/discussion.html", {"discussion": dis})


@require_POST
@login_required
def change_discussion_rating(request, slug):
	pass


@require_POST
@login_required
def change_comment_rating(request, id):
	pass


def load_more_comments(request, id):
	return None