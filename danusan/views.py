from django.shortcuts import render, redirect
from django.forms.models import model_to_dict
from django.urls import reverse
from django.http import HttpResponseBadRequest, JsonResponse
from .models import Danusan
from .forms import DanusanForm

from django.contrib.auth.decorators import login_required

# @login_required
def index(request):
	form = DanusanForm()
	context = {
		'generated_html' : form,
	}
	return render(request, 'index.html', context)

@login_required
def add_danusan(request):
	form = DanusanForm(request.POST)
	if (form.is_valid()):
		danusan = form.save(commit=False)
		danusan.user = request.user
		danusan.save()
		return JsonResponse(Danusan.objects.filter(id=danusan.id).values()[0])
	return HttpResponseBadRequest()

def get_danusan(request):
	return JsonResponse(list(Danusan.objects.all().values()), safe=False)

# def delete_danusan(request, id):
# 	danusan = Danusan.objects.get(id=id)
# 	danusan.delete()
# 	return redirect(reverse('index_danusan'))

from django.contrib.auth import authenticate

def login(request):
	user = authenticate(username='kezia', password='kezia')
	return redirect(reverse('index_danusan'))
