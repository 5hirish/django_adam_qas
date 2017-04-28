from django.shortcuts import render
from django.http import HttpResponseRedirect
from django import views
from .qclassifier import classify_question
# Create your views here.


def answer_question(question_str):

    answer = classify_question(question_str)
    return answer


class HomeView(views.View):

    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})

    def post(self, request, *args, **kwargs):
        question_str = request.POST.get("question", "")
        show_res = request.POST.get("switch_int_res", "False")
        print("Question:", question_str)
        print("Intermediate Results:", show_res)

        if not question_str == "":

            answer_question(question_str)

            return HttpResponseRedirect('/answer/')
        return render(request, self.template_name, {})


def features_view(request):
    return render(request, 'features.html', {})


def about_view(request):
    return render(request, 'about.html', {})
