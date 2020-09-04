from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.MainPageView.as_view()),
    path('login/', views.MainPageView.as_view()),
    path('signup/', views.MainPageView.as_view()),
    path('home/', views.MainPageView.as_view()),
    path('vacancies/', include('vacancy.urls')),
    path('resumes/', include('resume.urls')),
]
