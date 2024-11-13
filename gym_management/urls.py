# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from gym import views
from django.contrib import admin

router = DefaultRouter()
router.register(r'membership-types', views.MembershipTypeViewSet)
router.register(r'members', views.MemberViewSet)
router.register(r'subscriptions', views.SubscriptionViewSet)
router.register(r'payments', views.PaymentViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
