from django.urls import path
from . import views

urlpatterns = [
    path('', views.ResumeListView.as_view(), name="resume_lust"),
]