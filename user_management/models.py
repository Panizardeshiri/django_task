from django.db import models

from user_management.querysets import CustomerQuerySet


class Customer(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    phone = models.CharField(max_length=20)
    address = models.TextField()
    order_count = models.IntegerField(default=0)
    total_spending = models.DecimalField(max_digits=5,decimal_places=2)

    objects = CustomerQuerySet.as_manager()

    

    def __str__(self):
        return self.user.username


class Manager(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.user.username