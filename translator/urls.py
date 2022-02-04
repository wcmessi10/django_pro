from django.urls import  path
from . import views

app_name = "translator"
urlpatterns=[
    path('index/', views.index, name="index"),
]