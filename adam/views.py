from django.shortcuts import render
from django.http import HttpResponseRedirect
from django import views
from .qclassifier import classify_question
from .feature_extractor import extract_features
import spacy
# Create your views here.


def answer_question(question_str):

    en_nlp = spacy.load("en_core_web_md")       # Current : en_core_web_md

    qclass = classify_question(en_nlp, question_str)
    keywords = extract_features(en_nlp, question_str, qclass)
    
    return qclass


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

            answer = answer_question(question_str)

            return render(request, self.template_name, {'answer': answer})
        return render(request, self.template_name, {})


def features_view(request):
    return render(request, 'features.html', {})


def about_view(request):
    return render(request, 'about.html', {})
