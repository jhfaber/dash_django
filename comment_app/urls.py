from django.urls import path

from . import views

from django.urls import path, include


app_name = 'comment_app'
urlpatterns =[
    path('', views.index_lol, name='index'),    
    path('add', views.add, name='add'), 
    path('contact', views.contact, name='contact'),   
    path('update/<int:pk>', views.update, name='update'),  
    
    
]


