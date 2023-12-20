from rest_framework import serializers
from server.model.PostModel import PostModel

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostModel
        fields = ['__all__']    