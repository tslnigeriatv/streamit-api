from django.urls import path, include
from . import views



urlpatterns = [
    path('email/', views.my_email, name='email')
]

