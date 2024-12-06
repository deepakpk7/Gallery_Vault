from django.urls import path
from . import views
urlpatterns=[
    path('',views.user_login),
    path('index',views.index),
    path('register',views.register),
    path('upload',views.upload),
    path('logout',views.user_logout),
    
]