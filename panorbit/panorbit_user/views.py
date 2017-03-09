from django.shortcuts import render
from django.contrib.auth import logout
from django.shortcuts import redirect
from .forms import EditForm,IndexForm,SignInForm
from .models import PanorbitUser
from django.core.mail import send_mail
from django.contrib.auth import authenticate,login
from django.contrib.auth import logout as django_logout
from django.contrib.sessions.backends.db import SessionStore
from django.contrib.auth.decorators import login_required
import pyotp


def index(request):
    totp=pyotp.TOTP('base32secret3232')
    form = IndexForm(request.POST or None)
    if request.POST:
        email = request.POST.get('email')
        if form.is_valid():
            if authenticate(email=email):
                generate_otp=totp.now()
            else:
                user=PanorbitUser.objects.create_user(email=email)
                user.save()
                generate_otp=totp.now()
        message = "your verfication code is %s."%(generate_otp)
        send_mail(
        'OTP Verification',
        message,
        email,
        ['jagadish@example.com'],
        fail_silently=False,
        )
        request.session['email'] = email
        request.session['generate_otp'] = generate_otp
        return redirect('/signin')
    else:
        return render(request,"index.html",{"form":form})

def signin(request):
    email = request.session['email']
    generate_otp = request.session['generate_otp']
    form = SignInForm(request.POST or None)
    if request.POST:
        otp = request.POST.get('otp')
        user = authenticate(email=email)
        if user is not None or otp == generate_otp:
            login(request,user)
            return redirect('/welcome/')

    content = {
        "form":form,
        'generate_otp':generate_otp
    }
    return render(request,'signin.html',content)

@login_required
def welcome(request):
	return render(request,'welcome.html')

@login_required
def edit(request):
	form = EditForm(request.POST or None,instance=request.user)
	if form.is_valid():
		form.save()
		return redirect('/welcome')
	context={
		'form':form,
	}
	return render(request,'edit.html',{'form':form})

@login_required
def logout(request):
    django_logout(request)
    return redirect('/index/')

 