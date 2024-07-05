
from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import StudentApiView
# from .views import 

router = DefaultRouter()
router.register('student',StudentApiView)

urlpatterns = [
    path('admin/', admin.site.urls),

]
