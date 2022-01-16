from django.shortcuts import render
from django.views.generic import ListView
from rest_framework import viewsets
from rest_framework.decorators import action

from a2.models import ModelA, ModelB
from a2.serializers import ModelASerializer
from a2.serializers import ModelBSerializer


class ModelAList(ListView):
    model = ModelA
    # queryset = ModelB.objects.all()
    context_object_name = 'listA'
    template_name = 'a2/a2_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['modB'] = ModelB.objects.all()
        return context


class ModelAView(viewsets.ModelViewSet):
    queryset = ModelA.objects.all()
    serializer_class = ModelASerializer


class ModelBView(viewsets.ModelViewSet):
    queryset = ModelB.objects.all()
    serializer_class = ModelBSerializer
