from django.db import models
from django.contrib.auth.models import User

class MembershipType(models.Model):
    name = models.CharField(max_length=50)
    duration_days = models.IntegerField()  # Number of days for the membership duration
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Member(models.Model):
    # Link to user with a role attribute to distinguish between admin, member, or trainer
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='member', null=True, blank=True)
    full_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    status = models.CharField(
        max_length=20,
        choices=[
            ('ACTIVE', 'Active'),
            ('EXPIRED', 'Expired'),
            ('SUSPENDED', 'Suspended')
        ],
        default='ACTIVE'
    )

    def __str__(self):
        return self.full_name

class Subscription(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name="subscriptions")
    membership_type = models.ForeignKey(MembershipType, on_delete=models.PROTECT, related_name="subscriptions")
    start_date = models.DateField()
    end_date = models.DateField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.member.full_name} - {self.membership_type.name}"

class Payment(models.Model):
    subscription = models.ForeignKey(Subscription, on_delete=models.CASCADE, related_name="payments")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)
    payment_method = models.CharField(max_length=100)
    status = models.CharField(
        max_length=20,
        choices=[
            ('COMPLETED', 'Completed'),
            ('PENDING', 'Pending'),
            ('FAILED', 'Failed')
        ]
    )

    def __str__(self):
        return f"Payment of {self.amount} for {self.subscription.member.full_name} on {self.payment_date}"

    def get_receipt(self):
        return f"Receipt for payment of {self.amount} made on {self.payment_date}"

# Add role to User model (role could also be managed with Django Groups and Permissions for more advanced role management)
User.add_to_class('role', models.CharField(
    max_length=10,
    choices=[
        ('ADMIN', 'Admin'),
        ('MEMBER', 'Member'),
        ('TRAINER', 'Trainer')
    ],
    default='MEMBER'
))
