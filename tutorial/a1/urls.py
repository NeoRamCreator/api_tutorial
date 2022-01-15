from django.urls import path, include
from rest_framework.routers import DefaultRouter
from a1 import views

router = DefaultRouter()
router.register(r'app-a1', views.ModelAView)

urlpatterns = [
    path('', include(router.urls)),
]
