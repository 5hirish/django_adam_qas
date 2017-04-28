from django.shortcuts import render
from django.http import HttpResponseRedirect
from django import views
from .forms import QInputForm
# Create your views here.


class HomeView(views.View):

    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        question_form = QInputForm()
        return render(request, self.template_name, {'question_form': question_form})

    def post(self, request, *args, **kwargs):
        question_form = QInputForm(request.POST)
        if question_form.is_valid():
            return HttpResponseRedirect('/success/')
        return render(request, self.template_name, {'question_form': question_form})


def features_view(request):
    return render(request, 'features.html', {})


def about_view(request):
    return render(request, 'about.html', {})
