from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from first_app.models import Choice, Question # imports are relate to manage.py



#GENERIC VIEWS
class IndexView(generic.ListView):
    template_name = 'polls/index.html' # file that we send info
    context_object_name = 'questions' # its the name that receive the html {"questions":Question.objects.order_by('-pub_date')[:5]}
    # print("hola")
    # print(context_object_name)
    def get_queryset(self):
        """Return the last five published questions."""
        # return Question.objects.order_by('-pub_date')[:5]
        return Question.objects.order_by('-pub_date')[:5]

    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # context = {'questions': latest_question_list}
    # return render(request, 'index.html', context)


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    ... # same as above, no changes needed.