from django.shortcuts import render
from django.views.generic import View,TemplateView,ListView,DetailView
from basic_app import models

# Create your views here.

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['injectme'] = 'BASIC INJECTION!'
        return context

class SchoolListView(ListView):
    model = models.School 


class SchoolDetailView(DetailView):
    model = models.School
    template_name = 'basic_app/school_detail.html'

    


