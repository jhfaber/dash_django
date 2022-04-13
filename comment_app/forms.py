

from django.forms import ModelForm,Textarea

from django import forms
# from django import forms

from .models import Comment,TypeContact


from django.core.exceptions import ValidationError
from django.core.validators import validate_email

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)

        #assgin a class to the form
        widgets = {
            "text" : Textarea(attrs={"class":"form-input"})
        }


# CUSTOM FORM
class ContactForm(forms.Form):

    #initial
    name =  forms.CharField(initial="john",label="Name",  required=True)
    surname =  forms.CharField(initial="marin",required=True, max_length=10, min_length=2)
    phone =  forms.CharField(initial="3053426563",required=False, max_length=10, min_length=2)
    email = forms.CharField(initial="initial@gmail.com",validators=[validate_email])
    email2 = forms.EmailField(initial="initial2@gmail.com")
    agree = forms.BooleanField(required=False)
    date = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}),required=False)

    document= forms.FileField(required=False)
    image= forms.ImageField(required=False)
    # phone =  forms.RegexField(initial="John", regex="^[+]*[(]{0,1}[0-9]{1,4}[)]{0,1}[-\s\./0-9]*$")
    # name =  forms.CharField(initial="John",required=False)


    SEX = (
        (1,"Male"),
        (2,"Female"),
        (3,"Other")
    )
 
    sex = forms.ChoiceField(required=False,choices=SEX,initial=2)

    type_contact = forms.ModelChoiceField(required=False,queryset=TypeContact.objects.all())

