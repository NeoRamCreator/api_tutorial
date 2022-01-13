from django.urls import path, include
from rest_framework.routers import DefaultRouter
from a1 import views

router = DefaultRouter()
router.register(r'app-a1', views.ModelAView)
router.register(r'app-a1/(?P<pk>[0-9]+)$')

urlpatterns = [
    path('', include(router.urls)),
]
