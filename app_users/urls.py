# urls.py
from django.urls import path, include
from .views import RegisterAPIView, VerifyOTPAPIView, ProfileAPIView, WorkerViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'workers', WorkerViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('verify/', VerifyOTPAPIView.as_view(), name='verify_otp'),
    path('me/', ProfileAPIView.as_view(), name='user_profile'),
]
