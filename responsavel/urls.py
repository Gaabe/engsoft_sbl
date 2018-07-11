from django.urls import path
from responsavel import views

urlpatterns = [
    path('register/', views.register)
]
