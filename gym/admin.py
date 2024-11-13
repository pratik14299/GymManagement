from django.contrib import admin
from .models import MembershipType, Member, Subscription, Payment

admin.site.register(MembershipType)
admin.site.register(Member)
admin.site.register(Subscription)
admin.site.register(Payment)