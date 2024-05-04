from django.contrib import admin
from .models import User, Service, Order

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('phone', 'email')

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'fee')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'service', 'payment_status')