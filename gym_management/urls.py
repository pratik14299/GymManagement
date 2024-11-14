# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from gym import views
from django.contrib import admin
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

router = DefaultRouter()
router.register(r'membership-types', views.MembershipTypeViewSet)
router.register(r'members', views.MemberViewSet)
router.register(r'subscriptions', views.SubscriptionViewSet)
router.register(r'payments', views.PaymentViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Login
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # RefreshIfExpires
    
]
