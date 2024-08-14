from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentApiView

router = DefaultRouter()
router.register(r'student', StudentApiView, basename='student')

urlpatterns = [
    path('', include(router.urls)),
]
