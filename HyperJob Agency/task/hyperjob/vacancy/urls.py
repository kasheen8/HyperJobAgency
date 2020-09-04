from django.urls import path
from . import views

urlpatterns = [
    path('', views.VacancyListView.as_view(), name='vacancies_list'),
]