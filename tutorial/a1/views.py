from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action

from a1.models import ModelA
from a1.serializers import ModelASerializer


# @action(detail=True, methods=['post'])
class ModelAView(viewsets.ModelViewSet):
    queryset = ModelA.objects.all()
    serializer_class = ModelASerializer



