from django.urls import path  # noqa: F401

from . import views

app_name = 'main'

urlpatterns = [
    path("", views.index, name="index"),
    path("exception", views.exception, name="exception"),
]
