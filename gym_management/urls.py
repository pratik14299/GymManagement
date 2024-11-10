from django.urls import path, include
from rest_framework.routers import DefaultRouter
from gym.views import MemberViewSet, PaymentViewSet
from django.contrib import admin

router = DefaultRouter()
router.register(r'members', MemberViewSet)
router.register(r'payments', PaymentViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
