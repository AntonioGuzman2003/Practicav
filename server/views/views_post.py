from rest_framework.views import APIView
from rest_framework.response import Response
from server.model.PostModel import PostModel
from server.serializers.PostSerializer import PostSerializer
class getPosts(APIView):
    def get(self, request):
        posts = PostModel.objects.filter()
        serializer = PostSerializer(posts,many=True)
        return Response(serializer.data)        