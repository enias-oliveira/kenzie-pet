from rest_framework.response import Response
from rest_framework.views import APIView


class Animal(APIView):
    def get(self, request):
        return Response({"msg": "Hello Animals"})
