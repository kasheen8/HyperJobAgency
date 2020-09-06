from django.views import View
from django.shortcuts import render
from .models import Vacancy

class VacancyListView(View):
    def get(self, request, *args, **kwargs):
        model = Vacancy
        queryset = model.objects.all()
        return render(request, "vacancy_list.html", context={'vacancies': queryset})

