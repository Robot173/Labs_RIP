from django.shortcuts import render
from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Horse
# Create your views here.
class HorseListView(ListView):
    model = Horse

    def get_context_data(self, **kwargs):
        context = super(HorseListView, self).get_context_data(**kwargs)
        return context