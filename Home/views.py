from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import SignupForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.contrib.auth.forms import AuthenticationForm
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
import uuid, random, requests
from .models import Sessions
from django.shortcuts import get_object_or_404

def home(request):
    if request.user.is_authenticated:
        return(redirect('dashboard'))
    else:
        return(render(request,'home/home.html'))

def signupuser(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if (request.POST['password1'] == request.POST['password2']):
            try:
                user = form.save(commit=False)
                user.is_active = False
                user.save()
                current_site = get_current_site(request)
                mail_subject = 'Activate your Classroom Plus account.'
                message = render_to_string('home/acc_active_email.html', {'user': user,'domain': current_site.domain,'uid':urlsafe_base64_encode(force_bytes(user.pk)),'token':account_activation_token.make_token(user),})
                to_email = form.cleaned_data.get('email')
                email = EmailMessage(mail_subject, message, to=[to_email])
                email.send()
                return(render(request, 'home/success.html'))
            except IntegrityError:
                return(render(request, 'home/signup.html', {'form':SignupForm(), 'error':'That Username has already been taken. Please choose another Username.'}))
            except ValueError:
                return(render(request, 'home/signup.html', {'form':SignupForm(), 'error':'Please enter your details correctly.'}))
        else:
            return(render(request, 'home/signup.html', {'form':SignupForm(), 'error':'Passwords did not match'}))
    else:
        form = SignupForm()
    return(render(request, 'home/signup.html', {'form': form}))

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request,user)
        return(render(request,'home/dashboard.html',{'success':'Thank you for your email confirmation.'}))
    else:
        return(HttpResponse('Activation link is invalid!'))

def loginuser(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return(redirect('dashboard'))
        else:
            return(render(request,'home/login.html', {'form':AuthenticationForm()}))
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return(render(request,'home/login.html', {'form':AuthenticationForm(), 'error':'Username and Password did not match'}))
        else:
            login(request, user)
            return(redirect('dashboard'))

@login_required
def profile(request):
    return(render(request,'home/profile.html'))

@login_required
def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return(redirect('home'))

@login_required
def dashboard(request):
    return(render(request,'home/dashboard.html'))

@login_required
def new_session(request):
    if request.method == 'POST':
        current_site = get_current_site(request)
        user = request.user
        session_name = urlsafe_base64_encode(force_bytes(user.pk))+'/'+ account_activation_token.make_token(user)+'/'+str(random.randint(1,100))
        url = 'http://' + current_site.domain + '/session/' + session_name

        api_url = 'https://classroomplus.herokuapp.com/sessions/new'
        params = {'session_id': session_name, 'user_id': user.pk, 'user_name': user.username}
        post = requests.post(api_url, json=params)
        return(render(request,'home/dashboard.html',{'url':url}))

@login_required
def user_session(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        return(render(request,'home/session.html'))

@login_required
def makequiz(request,uidb64, token):
    return(render(request,'home/makeQuiz.html'))

@login_required
def quizresponse(request,uidb64, token):
    return(render(request,'home/getQuestionsStudents.html'))

@login_required
def icebreaker(request,uidb64, token):
    return(render(request,'home/icebreaker.html'))

@login_required
def freeresponse(request,uidb64, token):
    return(render(request,'home/answerOpenEnded.html'))
