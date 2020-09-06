from django.views import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView
from django.shortcuts import render, redirect
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from resume.models import Resume
from vacancy.models import Vacancy

class MainPageView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "menu.html")

class MySignupView(CreateView):
    form_class = UserCreationForm
    success_url = '/login'
    template_name = 'signup.html'

class MyLoginView(LoginView):
    form_class = AuthenticationForm
    redirect_authenticated_user = True
    template_name = 'login.html'

class NewPostForm(forms.Form):
    description = forms.CharField(min_length=10, max_length=1024)


class NewResumeView(View):
    def post(self, request, *args, **kwargs):
        request_user = User.objects.filter(username=request.user.username)[0]
        description = request.POST.get('description')
        Resume.objects.create(author=request_user, description=description)
        return redirect('/home')


class NewVacancyView(View):
    def post(self, request, *args, **kwargs):
        request_user = User.objects.filter(username=request.user.username)[0]
        description = request.POST.get('description')
        if request_user.is_staff:
            Vacancy.objects.create(author=request_user, description=description)
            return redirect('/home')
        raise PermissionDenied


class HomePageView(View):
    def get(self, request, *args, **kwargs):
        new_post_form = NewPostForm()
        return render(request, 'profile.html', {'form': new_post_form})

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            request_user = User.objects.filter(username=request.user.username)[0]
            if request_user.is_staff:
                return redirect('/vacancy/new')
            else:
                return redirect('/resume/new')
        else:
            raise PermissionDenied


