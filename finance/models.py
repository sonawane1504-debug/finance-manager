from pyexpat import model
from django.db import models
from django.contrib.auth.models import User   
from django.db.models import CASCADE


class Transaction(models.Model):
    # We need choices for types (Income or Expenses)
    TRANSACTION_TYPES = [
        ('income', 'Income'),
        ('expense', 'Expense'),
    ]

    # Link field
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # Define the columns of out table
    title = models.CharField(max_length = 100)  #e.g., "Salary" or "Pizza"
    amount = models.DecimalField(max_digits=10, decimal_places=2) #e.g., 150.50
    type = models.CharField(max_length=10, choices=TRANSACTION_TYPES)
    date = models.DateField(auto_now_add=True) #Automatically set today's date

    # This make it look nice in the Admin panel
    def __str__(self):
        return f"{self.title} - {self.amount}"