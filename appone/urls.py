from django.urls import path
from . import views

urlpatterns = [
    path("", views.indexPageView, name="index_page"),
]