from django.db import models

import datetime


from rest_api.models import Element
# Create your models here.


class Comment(models.Model):
    text =  models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    element = models.ForeignKey(Element, related_name='comments',on_delete=models.CASCADE,null=True)


    def __str__(self):
        return 'Comentario #{}: {}'.format(self.id,self.text)
    


class Contact(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    email = models.CharField(max_length=70)
    phone = models.CharField(max_length=13)
    date_birth = models.DateField(null=True, default=datetime.date.today)
    document = models.FileField(upload_to="uploads/contact")
    

class TypeContact(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return '{}'.format(self.name)
