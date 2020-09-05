from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin



class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'app/calculation.html'
    login_url = '/accounts/login/'

class AbtView(TemplateView):
    template_name = 'about.html'