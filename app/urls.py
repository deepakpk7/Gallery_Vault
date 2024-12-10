from django.urls import path
from . import views
urlpatterns=[
    path('',views.user_login),
    path('index',views.index),
    path('register',views.register),
    path('upload',views.upload),
    path('delete/<pid>',views.file_delete),
    path('logout',views.user_logout),
    
]