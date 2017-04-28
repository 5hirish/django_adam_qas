from django.shortcuts import render
from django import views
from .forms import QInputForm
# Create your views here.


class HomeView(views.View):

    def get(self):
        question_form = QInputForm()
        return render()
