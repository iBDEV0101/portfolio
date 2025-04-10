from django.urls import path
from .views import index, template, home

urlpatterns = [
    path("home",template , name="index"),
    path('', home, name='home'),
    path('template',index, name="blog-index")
]