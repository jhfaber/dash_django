from django.shortcuts import get_object_or_404, render
from django.http import Http404

# from django.http import HttpResponse
from django.template import loader

from .models import Choice, Question
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# Create your views here.



#BASI USE 
# def index(request):
#     print("ok")
#     return HttpResponse("Hola mundo")

# USE DATABASE
# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     output = ', '.join([q.question_text for q in latest_question_list])
    
#     return HttpResponse(output)





def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'questions': latest_question_list}
    return render(request, 'index.html', context)



def detail(request, question_id):
    #Get his id o 404 error
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'detail.html', {'question': question})


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'first_app/results.html', {'question': question})

    # return HttpResponse("Hola mundo")


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    print(question)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])

        
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'first_app/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('first_app:results', args=(question.id,)))