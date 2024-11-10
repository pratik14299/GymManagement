from django.db import models
from django.contrib.auth.models import User

# Define Membership Types
class Member(models.Model):
    MEMBERSHIP_TYPES = (
        ('monthly', 'Monthly'),
        ('yearly', 'Yearly'),
    )

    # Add user (trainer assigns the user)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='member', null=True, blank=True)
    full_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    membership_type = models.CharField(max_length=10, choices=MEMBERSHIP_TYPES)
    membership_start_date = models.DateField()
    membership_end_date = models.DateField()

    def __str__(self):
        return self.full_name


class Payment(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)
    payment_method = models.CharField(max_length=100)

    def __str__(self):
        return f"Payment of {self.amount} for {self.member.full_name} on {self.payment_date}"

    def get_receipt(self):
        return f"Receipt for payment of {self.amount} made on {self.payment_date}"
