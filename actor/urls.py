from django.urls import path

from .views import ActorsListView

urlpatterns = [
    path('list/', ActorsListView.as_view(), name='actors-list')
]