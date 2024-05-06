from django.urls import path
from . import views

urlpatterns = [
    path('', views.register, name='register'),
    path('services/', views.list_services, name='list_services'),
    path('place-order/', views.place_order, name='place_order'),
    path('process-payment/<int:order_id>/', views.process_payment, name='process_payment'),
]
