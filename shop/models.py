from django.db import models

# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=50)  # First name of the customer
    last_name = models.CharField(max_length=50)   # Last name of the customer
    email = models.EmailField(unique=True)        # Email (unique for each customer)
    phone_number = models.CharField(max_length=15, blank=True, null=True)  # Optional phone number
    created_at = models.DateTimeField(auto_now_add=True)  # When the customer was created

    def __str__(self):
        return f"{self.first_name} {self.last_name}"  # How to display the customer in the admin panel

# Define the Order model
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="orders")  # One-to-many relationship
    order_date = models.DateTimeField(auto_now_add=True)  # When the order was placed
    status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Completed', 'Completed')], default='Pending')  # Order status
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)  # Total cost of the order

    def __str__(self):
        return f"Order #{self.id} for {self.customer.first_name} {self.customer.last_name}"