from rest_framework import serializers

from a1.models import ModelA


class ModelASerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = ModelA
        fields = ['pk', 'url', 'a1', 'a2', 'a3', 'a4', ]

