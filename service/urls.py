from django.urls import path
from .views import SalonsView, CreateUsersView, UsersView


urlpatterns = [
    path('salon/', SalonsView.as_view()),
    path('register/', CreateUsersView.as_view()),
    path('users/', UsersView.as_view()),
]