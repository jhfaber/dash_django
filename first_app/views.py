from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.


def index(request):
    print("ok")
    return HttpResponse("Hola mundo")


def detail(request, question_id):

    '''try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404('Pregunta no existe')'''

    # question = get_object_or_404(Question, pk=question_id)

    # return render(request,'detail.html',{'question':question,})

    return HttpResponse("Detail %s" % question_id)

def results(request, question_id):
    # question = get_object_or_404(Question, pk=question_id)
    # return render(request,'results.html',{'question':question,})
    return HttpResponse("Results %s" % question_id)