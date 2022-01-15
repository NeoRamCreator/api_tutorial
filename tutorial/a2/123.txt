from rest_framework import serializers

from a2.models import ModelA
from a2.models import ModelB


class ModelASerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ModelA
        fields = ['pk', 'url', 'a1', 'a2', 'a3', 'a4', ]


class ModelBSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ModelB
        fields = ['pk', 'url', 'a1', 'a2', 'a3', 'a4', ]
