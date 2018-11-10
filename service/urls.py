from django.urls import path
from .views import (SalonView, CreateUserView, UserView, ServiceView,
        ProfileView, MasterView, MasterDetailView)

urlpatterns = [
    path('register/', CreateUserView.as_view()),
    path('users/', UserView.as_view()),
    path('salons/', SalonView.as_view()),
    path('services/', ServiceView.as_view()),
    path('profile/', ProfileView.as_view()),
    path('masters/', MasterView.as_view()),
    path('masters/<int:pk>/', MasterDetailView.as_view())
]