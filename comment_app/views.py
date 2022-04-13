from django.shortcuts import render,redirect, get_object_or_404

from django.http import HttpResponseRedirect
from django.contrib import messages


from .models import Comment,Contact
from .forms import CommentForm, ContactForm
# Create your views here.




def index_lol(request):
    comments = Comment.objects.all()

    return render(request,'comment_app/index.html', {'comments':comments})



def add(request):

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            # return redirect("comment:index")
            # return render(request,'comment_app/index.html')
            return HttpResponseRedirect('/comment')
    else:
        form = CommentForm()
    
    return render(request,'comment_app/add.html', {'form':form})


def update(request, pk):

    comment =  get_object_or_404(Comment,pk=pk)

    if request.method == "POST":
        form = CommentForm(request.POST, instance = comment)

        # watch errors
        print(form.errors.as_json())

        if form.is_valid():
            form.save()
            # return redirect("comment:index")
            # return render(request,'comment_app/index.html')
            return HttpResponseRedirect('/comment')
    else:
        form = CommentForm(instance = comment)
    
    return render(request,'comment_app/update.html', {'form':form,"comment":comment})




def contact(request):
    form = ContactForm()

    if request.method == "POST":
        # form = ContactForm(request.POST)
        form = ContactForm(request.POST, request.FILES) #received files

        # print(form.errors.as_json())
        print(form.is_valid())

        
        if form.is_valid():

            #GET DATA FROM FORM

            print(request.FILES)
            # print(form.cleaned_data["name"])

            contact = Contact()
            contact.name = form.cleaned_data["name"]
            contact.surname =  form.cleaned_data["surname"]
            contact.phone =  form.cleaned_data["phone"]
            contact.email =  form.cleaned_data["email"]
            

            # print(form.cleaned_data["type_contact"].name)
            print(form.cleaned_data["sex"])

            # contact.date_birth =  form.cleaned_data["date"]
            if "date" in form.cleaned_data:
                contact.date_birth =  form.cleaned_data["date"]
            if "document" in request.FILES:
                contact.document =  request.FILES["document"]
            
            contact.save()

            messages.add_message(request, messages.INFO, "Contact created!")

            # redirect("comment_app/index")
            return HttpResponseRedirect('/comment/contact')
        else:
            form = ContactForm()
    
    return render(request,'comment_app/contact.html', {'form':form})