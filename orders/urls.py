from django.urls import path
from . import views

urlpatterns = [
    path("orders/", views.OrderView.as_view()),
    path("orders/<int:pk>/", views.OrderUpdateView.as_view()),
    path("orders/seller/", views.OrderGetView.as_view()),
]
