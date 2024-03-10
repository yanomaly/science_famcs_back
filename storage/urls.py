from django.urls import path

from .views import SearchRetrieveView

app_name = 'storage'
urlpatterns = [
    path('file/', SearchRetrieveView.as_view()),
]
