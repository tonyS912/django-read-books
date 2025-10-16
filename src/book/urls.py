from django.urls import path
from . import views

# Create your URL's here
urlpatterns = [
    path("", views.book, name="book"),
]
