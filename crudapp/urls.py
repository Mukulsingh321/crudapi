from django.urls import path
from crudapp import views

urlpatterns =[
    path('', views.crudapi.as_view()),
    path('crud/<int:pk>/', views.crud_pk.as_view()),
]