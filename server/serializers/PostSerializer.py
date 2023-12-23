from rest_framework import serializers
from server.model.PostModel import PostModel
from server.serializers.CategoriaSerializer import CategoriaSerializer
class PostSerializer(serializers.ModelSerializer):
    categoria = CategoriaSerializer()
    class Meta:
        model = PostModel
        fields = ['id','titulo','descripcion','picture','categoria']    