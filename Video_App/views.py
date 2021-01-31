from django.shortcuts import render, redirect
from .models import Video
from .models import Detail
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from PIL import Image


# Create your views here.
def Index(request):
    detail = Detail.objects.all()
    return render(request, 'index.html', {"detail": detail})


def getRegistration(request):
    if request.user.is_authenticated:
        return redirect('index')
    
    else:
        form = CreateUserForm()
        if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.info(request, 'This Account Is Created Successfully!'+' '+ user)
                return redirect('login')
        context={"form":form}
        return render(request, 'registration.html', context)


def getLogin(request):
    if request.user.is_authenticated:
        return redirect('index')

    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password= request.POST.get('password')

            user = authenticate(request, username = username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, 'User Login Successfull')
                return redirect('index')
            else:
                messages.info(request, 'username or password incorrect!')
                return redirect('index')

        context={}
        return render(request, 'login.html', context)


def getlogout(request):
    logout(request)
    messages.info(request, 'User Logout Successfull')
    return redirect('index')

@login_required(login_url='login')
def VideoTutorial(request):
    video = Video.objects.all()
    return render(request, 'video.html', {"video":video})
