from django.urls import path 
from . import views

urlpatterns = [
    path('' , views.home, name="signup"),
    path('activities' , views.all_activity, name="all_activity"),

]