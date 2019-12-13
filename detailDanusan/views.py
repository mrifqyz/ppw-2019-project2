from django.shortcuts import render, redirect
from django.http import JsonResponse
# import requests
from .forms import ReviewForm
from .models import ReviewModel
from danusan.models import Danusan

def detail_danusan(request, slug):
	'''buat dapetin detail'''
	danusan = list(Danusan.objects.filter(slug=slug))
	if(len(danusan)!=0):

	# print(danusan)
		review = ReviewModel.objects.filter(detail=danusan[0])
		formTulis = ReviewForm()
		args = {
			'danusan':danusan[0],
			'reviewForm':formTulis,
			'review':review
		}

		return render(request, 'detail.html', args)
	else:
		return redirect('/danusan')

def buat_review(request):
	review = ReviewForm(request.POST)
	toSave = review.save(commit = False)
	toSave = request.danusan
	print(request.POST)
	toSave.save()
	return JsonResponse({'status':'200'})

def nampilin_review(request):
	reviewModel = ReviewModel.objects.all()
	args = {
		'reviewModel' : reviewModel,
	}
	return render(request, 'detail.html', args)




