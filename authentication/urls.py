from django.urls import path

from .views import RegistrationView, LoginView, UserRetrieveUpdateView

app_name = 'authentication'
urlpatterns = [
    path('user', UserRetrieveUpdateView.as_view()),
    path('users/', RegistrationView.as_view()),
    path('users/login/', LoginView.as_view()),
]
