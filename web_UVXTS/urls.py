from django.urls import path
from . import views

urlpatterns = [
     path('', views.index, name="index"),
     path('blog.html', views.blog, name="blog"),
     # path('blog-single.html', views.blog-single, name="blog-single"),
     path('home.html', views.home, name="home"),
     path('contact.html', views.contact, name="contact"),
     path('about.html', views.about, name="about"),
     path('gallery.html', views.gallery, name="gallery"),
     path('index.html', views.index, name="index"),
     # path('', views.my_form, name='my_form')
]
