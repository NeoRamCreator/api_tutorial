from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action

from a2.models import ModelA, ModelB
from a2.serializers import ModelASerializer
from a2.serializers import ModelBSerializer


class ModelAView(viewsets.ModelViewSet):
    queryset = ModelA.objects.all()
    serializer_class = ModelASerializer


class ModelBView(viewsets.ModelViewSet):
    queryset = ModelB.objects.all()
    serializer_class = ModelBSerializer
