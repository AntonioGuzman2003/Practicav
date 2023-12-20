from rest_framework import serializers
from server.model.CategoriaModel import CategoriaModel

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaModel
        fields = ['__all__']    