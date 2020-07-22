from django.conf.urls import url
from django.urls import path
from prac3app  import views
urlpatterns=[
path('', views.index, name='index'),
path('form/',views.form, name='form'),
path('signup/',views.signup_forms, name='signup'),
]
