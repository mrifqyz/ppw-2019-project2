from django.shortcuts import render, redirect, reverse
from .forms import LoginForm, RegisterForm
from django.contrib.auth import login, logout, authenticate
from .models import User
from danusan.models import Danusan

# Create your views here.
def loginPage(request):
    if(request.method == 'POST'):
        form = LoginForm(request.POST)

        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if(user is not None ):  
            login(request, user);   
            request.session.set_expiry(7200)
            return redirect('/kelola')

    else:
        form = LoginForm()
    return render(request, 'login.html', {'form':form})

def registerPage(request):
    if(request.method == 'POST'):
        form = RegisterForm(request.POST)
        # print('tes1')
        if(form.is_valid()):
            # print('tes1')
            email = request.POST['username']
            fullname = request.POST['fullname']
            bio = request.POST['bio']
            phone = request.POST['phone']
            password = form.clean_password2()
            
            User.objects.create_user(email, fullname, bio, phone, password)
            return redirect('/login')
    else:
        form = RegisterForm

    return render(request, 'register.html', {'form':form})

def managePage(request):
    if(request.user.is_authenticated):
        listDanusanUser = Danusan.objects.filter(user=request.user)[:3]
        data = {
            'danusan':listDanusanUser
        }
        return render(request, 'kelola.html', data)

    return render(request, 'kelola.html')

def signOut(request):
    logout(request)
    return redirect(reverse(loginPage))