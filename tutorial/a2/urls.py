from django.urls import path, include
from rest_framework.routers import DefaultRouter
from a2 import views

router = DefaultRouter()
router.register(r'mod-a', views.ModelAView)
router.register(r'mod-b', views.ModelBView)

urlpatterns = [
    path('', include(router.urls)),
]
