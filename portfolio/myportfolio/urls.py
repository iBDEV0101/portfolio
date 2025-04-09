from django.urls import path
from .views import index, template, home

urlpatterns = [
    path("",template , name="index"),
    path('home', home, name='home'),
    path('template',index, name="blog-index")
]