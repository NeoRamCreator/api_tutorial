from rest_framework import serializers

from a1.models import ModelA


# class ModelASerializer(serializers.ModelSerializer):
class ModelASerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='a-detail', read_only=True)

    class Meta:
        model = ModelA
        fields = ['pk', 'url', 'a1', 'a2', 'a3', 'a4', ]

