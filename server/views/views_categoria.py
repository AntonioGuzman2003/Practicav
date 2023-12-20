from rest_framework.views import APIView
from rest_framework.response import Response
from server.model.CategoriaModel import CategoriaModel
from server.serializers.CategoriaSerializer import CategoriaSerializer
class getCategorias(APIView):
    def get(self, request):
        categorias = CategoriaModel.objects.filter()
        serializer = CategoriaSerializer(categorias,many=True)
        return Response(serializer.data)        