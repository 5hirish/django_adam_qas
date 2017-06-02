from django.shortcuts import render
from django.http import HttpResponseRedirect
from django import views
from .qa_init import answer_question
from time import time
from spacy import load
# Create your views here.


def get_answer(question_str):

    start_time = time()

    answer_output, intermediate_results = answer_question(question_str)

    end_time = time()

    total_time = end_time - start_time

    print("Total time :", total_time)

    exec_time = "Time: " + str(total_time) + " secs."

    return answer_output, exec_time, intermediate_results


class HomeView(views.View):

    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        answer = "Ask me a question and I'll answer..."
        exec_time = "Time: 00.00 secs."
        return render(request, self.template_name, {'answer': answer, 'time': exec_time})

    def post(self, request, *args, **kwargs):
        answer = "Ask me a question and I'll answer..."
        exec_time = "Time: 00.00 secs."
        question_str = request.POST.get("question", "")
        print("Question:", question_str)

        if not question_str == "":

            answer, exec_time, intermediate_results = get_answer(question_str)
            request.session['results'] = intermediate_results

            return render(request, self.template_name, {'answer': answer, 'time': exec_time})
        return render(request, self.template_name, {'answer': answer, 'time': exec_time})


def features_view(request):
    return render(request, 'features.html', {})


def results_view(request):
    try:
        results = request.session['results']
    except KeyError:
        results = ["Intermediate Results..."]
    return render(request, 'results.html', {'results': results})


def about_view(request):
    return render(request, 'about.html', {})
