from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('api/', views.homepage_api, name='homepage_api'),
    path('candidates/', views.candidates, name='candidates'),
    path('candidates/<int:id>', views.candidate, name='candidate'),
]
