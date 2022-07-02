from django.urls import path
from news import views

urlpatterns = [
    path('',views.home,name='home'),
    path('about_detail/<int:pk>',views.about_detail,name='about_detail'),
]