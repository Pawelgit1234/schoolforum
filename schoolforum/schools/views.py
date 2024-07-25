from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_GET
from django.views.decorators.csrf import csrf_exempt

import json

from .models import School, Discussion, Rating, Comment


def home_view(request):
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


def school_view(request, slug):
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

	return render(request, 'schools/search_results.html', {'query': query})


def load_searched_objects(request):
	offset = int(request.GET.get('offset', 0))
	query = request.GET.get('query')

	schools_raw = School.objects.filter(name__contains=query)[offset:offset+10]
	discussions_raw = Discussion.objects.filter(title__contains=query)[offset:offset+10]

	schools = []
	discussions = []

	for school in schools_raw:
		schools.append({
			"photo_url": school.photos.all()[0].image.url if school.photos.exists() else '',
			"name": school.name,
			"description": school.description[:100] + '...',
			"slug": school.slug,
		})

	for discussion in discussions_raw:
		discussions.append({
			"title": discussion.title,
			'user': discussion.user.username,
			'avatar': discussion.user.profile.avatar.url,
			'created_at': discussion.created_at.strftime("%Y-%m-%d %H:%M:%S"),
			'lesson_type': discussion.lesson_type,
			'rating': discussion.overall_rating_balance(),
			'comments_count': discussion.discussion_comments.count(),
			'is_closed': discussion.is_closed,
			'id': discussion.id
		})

	response = {
		"schools": schools,
		"discussions": discussions,
		"found_count": len(schools) + len(discussions),
	}
	return JsonResponse(response)

def discussion_view(request, id):
	discussion = get_object_or_404(Discussion, id=id)
	user = request.user

	if user.is_authenticated:
		arrow_up = discussion.ratings.filter(user=user, is_plus=True).exists()
		arrow_down = discussion.ratings.filter(user=user, is_plus=False).exists()
	else:
		arrow_up = False
		arrow_down = False

	context = {
		'discussion': discussion,
		'arrow_up': not arrow_up,
		'arrow_down': not arrow_down,
	}

	return render(request, 'schools/discussion.html', context)


@require_POST
@login_required
@csrf_exempt
def change_discussion_rating(request):
	data = json.loads(request.body)
	discussion_id = data.get('id')
	is_up_arrow = data.get('is_up_arrow')

	discussion = get_object_or_404(Discussion, id=discussion_id)
	user = request.user

	rating, created = Rating.objects.get_or_create(user=user, discussion=discussion)

	if rating.is_plus == is_up_arrow:
		rating.is_plus = None
		rating.save()
	else:
		rating.is_plus = is_up_arrow
		rating.save()

	new_rating_balance = discussion.overall_rating_balance()

	return JsonResponse({'status': 'success', 'new_rating': str(new_rating_balance), 'is_up': rating.is_plus})


def load_more_comments(request, id):
	offset = int(request.GET.get('offset', 0))
	limit = 10
	comments = Comment.objects.filter(discussion_id=id, parent=None).order_by('created_at')[offset:offset+limit]
	comments_data = []

	for comment in comments:
		replies = comment.replies.all()
		replies_data = [
			{
				'id': reply.id,
				'user': reply.user.username,
				'avatar': reply.user.profile.avatar.url,
				'created_at': reply.created_at.strftime("%Y-%m-%d %H:%M:%S"),
				'content': reply.content,
				'photos': [photo.image.url for photo in reply.photos.all()]
			} for reply in replies
		]
		comments_data.append({
			'id': comment.id,
			'user': comment.user.username,
			'avatar': comment.user.profile.avatar.url,
			'created_at': comment.created_at.strftime("%Y-%m-%d %H:%M:%S"),
			'content': comment.content,
			'replies': replies_data,
			'photos': [photo.image.url for photo in comment.photos.all()]
		})

	return JsonResponse(comments_data, safe=False)
