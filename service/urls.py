from django.urls import path
from .views import (SalonView, CreateUserView, UserView, ServiceView,
        ProfileView, MasterView, MasterDetailView, ServiceAndTime, OrderView, 
        OrderDetailView, MastersOrderView, ServiceAndSalon, VerifyPhone)

urlpatterns = [
    path('register/', CreateUserView.as_view()),
    path('profile/', ProfileView.as_view()),
    
    path('users/', UserView.as_view()),
    path('users/verify/', VerifyPhone.as_view()),

    path('salons/', SalonView.as_view()),
    path('services/', ServiceView.as_view()),

    path('masters/', MasterView.as_view()),
    path('masters/<int:pk>/', MasterDetailView.as_view()),
    path('masters/orders/', MastersOrderView.as_view()),
    
    path('orders/', OrderView.as_view()),
    path('orders/<int:pk>/', OrderDetailView.as_view()),

    path('service/time/', ServiceAndTime.as_view()),
    path('service/salon/', ServiceAndSalon.as_view()),
]