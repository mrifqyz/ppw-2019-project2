from django.shortcuts import render, redirect, HttpResponse
from django.core import serializers
import json
# import requests
from .forms import ReviewForm
from .models import ReviewModel
from danusan.models import Danusan

def detail_danusan(request, slug):
	'''buat dapetin detail'''
	danusan = Danusan.objects.filter(slug=slug)
	if(len(danusan)!=0):
		review = ReviewModel.objects.filter(detail=list(danusan)[0])
		if(request.method == "POST"):
			form = ReviewForm(request.POST)
			if(form.is_valid()):
				print('success')
				ReviewModel.objects.create(
					Nama = request.POST['nama'],
					Review = request.POST['review'],
					detail = list(danusan)[0]
					)

				return redirect('/danusan/'+slug)
		else:
			formTulis = ReviewForm()
			args = {
				'danusan':danusan[0],
				'reviewForm':formTulis,
				'reviewModel':review
			}
			return render(request, 'detail.html', args)
	else:
		return redirect('/danusan')

def reviewToAPI(request, danusan):
	if(danusan=="all"):
		listReview = ReviewModel.objects.all()
	else:
		danusanObject = Danusan.objects.filter(slug=danusan)
		listReview = ReviewModel.objects.filter(detail=list(danusanObject)[0])
	jsonReview = serializers.serialize("json", listReview)
	data = json.loads(jsonReview)
	toBeReturned = json.dumps(data)
	return HttpResponse(toBeReturned, content_type="application/json")




