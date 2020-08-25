from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            User.objects.create_user(username=form.instance.username,
                                      password=form.instance.password,
                                      email=form.instance.email,
                                      last_name=form.instance.last_name,)
            user=User.objects.get(username=form.instance.username)

            return redirect('/')
        else:
            return redirect('sign_up')
    else:
        form=SignUpForm
    return render(request,'accounts/sign_up.html',{
        'form':form,
    })

def sign_in(request):
    if request.method =='POST':
        u_id = request.POST['u_id']
        u_pw = request.POST['u_pw']
        user = authenticate(request,username=u_id, password=u_pw)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return redirect('sign_in')
    else:
        return render(request,'accounts/sign_in.html')

def sign_out(request):
    logout(request)
    return redirect('/')



