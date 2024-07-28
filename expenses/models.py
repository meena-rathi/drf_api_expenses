# from django.db import models
#from django.contrib.auth.models import User

# class Category(models.Model):
#     name = models.CharField(max_length=100)

#     def __str__(self):
#         return self.name

# class Expense(models.Model):
#     amount = models.DecimalField(max_digits=10, decimal_places=2)
#     description = models.TextField()
#     category = models.ForeignKey(Category, on_delete=models.CASCADE)
#     date = models.DateField(auto_now_add=True)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)

#     def __str__(self):
#         return f"{self.amount} - {self.description} - {self.category.name}"

from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Expense(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Ensure this line is correct

    def __str__(self):
        return f"{self.amount} - {self.description}"

class Budget(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f'Budget: {self.amount} | Balance: {self.balance}'