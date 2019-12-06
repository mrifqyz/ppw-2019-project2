from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Danusan
from .forms import DanusanForm

from django.contrib.auth.decorators import login_required

def index(request):
	danusan_form = DanusanForm()
	context = {
		'danusans' : Danusan.objects.all(),
		'generated_html' : danusan_form,
	}
	return render(request, 'index.html', context)

# @login_required
def add_danusan(request):
	danusan = DanusanForm(request.POST)
	danusan.user = request.user
	danusan.save()
	return redirect(reverse('index_danusan'))

# def delete_danusan(request, id):
# 	danusan = Danusan.objects.get(id=id)
# 	danusan.delete()
# 	return redirect(reverse('index_danusan'))

from django.contrib.auth import authenticate

def login(request):
	user = authenticate(username='kezia', password='kezia')
	return redirect(reverse('index_danusan'))
