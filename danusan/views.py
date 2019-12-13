from django.shortcuts import render, redirect, HttpResponse
from django.forms.models import model_to_dict
from django.urls import reverse
from django.http import HttpResponseBadRequest, JsonResponse
from .models import Danusan
from .forms import DanusanForm
from django.core import serializers
import json
from django.contrib.auth import authenticate

from django.contrib.auth.decorators import login_required

@login_required
def add_danusan(request):
    form = DanusanForm(request.POST)
    if(form.is_valid()):
        danusan = form.save(commit = False)
        danusan.user = request.user
        form.save()
    return redirect(reverse('index_danusan'))

# @login_required
def index(request):
	form = DanusanForm()
	context = {
		'generated_html' : form,
	}
	return render(request, 'index.html', context)

def get_danusan(request):
	return JsonResponse(list(Danusan.objects.all().values()), safe=False)

# def delete_danusan(request, id):
# 	danusan = Danusan.objects.get(id=id)
# 	danusan.delete()
# 	return redirect(reverse('index_danusan'))


# def add_danusan(request):
#     danusan = DanusanForm(request.POST)
#     if(danusan.is_valid()):
#         Danusan.objects.create(
#             image=request.POST["image"],
#             name=request.POST["nama"],
#             price=request.POST["harga"],
# 			user=request.user
#         )
#     return redirect(reverse('index_danusan'))


def login(request):
    user = authenticate(username='kezia', password='kezia')
    return redirect(reverse('index_danusan'))

def danusanJSON(request, kw="", val=""):
    if(kw=="all" and val=="no_keyword"):
        listDanusan = Danusan.objects.all()
    elif(kw=="name" and val!=""):
        listDanusan = Danusan.objects.filter(name__contains=val)
    elif(kw=="user" and val == "current"):
        if(request.user.is_authenticated):
            listDanusan = Danusan.objects.filter(user=request.user)
        else:
            listDanusan = Danusan.objects.all()
    else:
        listDanusan = Danusan.objects.all()

    jsonDanusan = serializers.serialize("json", listDanusan)
    data = json.loads(jsonDanusan)
    toBeReturned = json.dumps(data)
    return HttpResponse(toBeReturned, content_type="application/json")

def detailReview(request):
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