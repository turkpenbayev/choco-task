from django.urls import path
from .views import (SalonsView, CreateUsersView, UsersView, ServicesView,
        ProfilesView)

urlpatterns = [
    path('register/', CreateUsersView.as_view()),
    path('users/', UsersView.as_view()),
    path('salons/', SalonsView.as_view()),
    path('services/', ServicesView.as_view()),
    path('profiles/', ProfilesView.as_view()),
]