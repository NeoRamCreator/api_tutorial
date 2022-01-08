from django.contrib import admin
from django.urls import path, include

from snippets import views

from rest_framework import routers

# router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)

urlpatterns = [
    # path('q', include(router.urls)),
    path('admin/', admin.site.urls),
    path('', include('snippets.urls')),

]
