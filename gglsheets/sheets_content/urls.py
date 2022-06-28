from django.urls import path
from . import views
from .views import PersonListView

urlpatterns = [ 
    path("", PersonListView.as_view()),
]