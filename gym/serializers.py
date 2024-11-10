from rest_framework import serializers
from .models import Member, Payment

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ['id', 'full_name', 'phone_number', 'membership_type', 'membership_start_date', 'membership_end_date']

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['id', 'member', 'amount', 'payment_date', 'payment_method']
