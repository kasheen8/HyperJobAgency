from django.views import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView
from django.shortcuts import render

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

