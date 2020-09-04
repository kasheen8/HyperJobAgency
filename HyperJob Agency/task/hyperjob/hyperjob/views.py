from django.views import View
from django.shortcuts import render

class MainPageView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "menu.html")