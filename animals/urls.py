from django.urls import path
from .views import Animal

urlpatterns = [path("animals/", Animal.as_view())]
