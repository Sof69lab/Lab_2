from django.urls import path
from pages import views

urlpatterns = [
    path("", views.MessageView.as_view(), name='list'),
    path("create/", views.createMessage, name='create'),
    path("registration/", views.registration, name='registration')
]