from django.views import View
from django.shortcuts import render
from .models import Resume

class ResumeListView(View):
    def get(self, request, *args, **kwargs):
        model = Resume
        queryset = model.objects.all()
        return render(request, "resume_list.html", context={'resume':queryset})
