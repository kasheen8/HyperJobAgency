from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.MainPageView.as_view()),
    path('vacancies/', include('vacancy.urls')),
    path('resumes/', include('resume.urls')),
    path('login', views.MyLoginView.as_view()),
    path('signup', views.MySignupView.as_view()),
    path('home/', views.MainPageView.as_view()),
    path('login/', RedirectView.as_view(url='/login')),
    path('signup/', RedirectView.as_view(url='/signup')),
]
