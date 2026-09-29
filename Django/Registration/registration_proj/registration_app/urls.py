from django.urls import path
from . import views

urlpatterns = [
    path('/', views.registration_app, name='registration_app'),
]