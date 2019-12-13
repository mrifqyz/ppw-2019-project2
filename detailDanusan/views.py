from django.shortcuts import render, redirect
# import requests
from .forms import ReviewForm
from .models import ReviewModel
from danusan.models import Danusan

def main(request):
	reviewModel = ReviewModel.objects.all()
	reviewForm = ReviewForm(request.POST or None)
	if request.method == 'POST':
		if reviewForm.is_valid():
			reviewForm.save()
			return redirect('/')

	args = {
		'reviewModel' : reviewModel,
		'reviewForm' : reviewForm,
	}

	return render(request, 'detail.html', args)

