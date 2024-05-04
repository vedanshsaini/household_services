from django.db import models

class User(models.Model):
    phone = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.phone} ({self.email})"

class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    fee = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    payment_status = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user} - {self.service.name}"