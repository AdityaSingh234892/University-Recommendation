from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index, name="index"),
   # path('', views.study_view, name="study_view"),
    #path('study/', views.study, name="study"),
    path('toprank/', views.toprank, name="toprank")
]