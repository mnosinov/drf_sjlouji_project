from rest_framework.views import APIView
from rest_framework.response import Response


class HelloAPI(APIView):
    def get(self, request, format=None):
        name = request.query_params.get('name')
        return Response({'response': f'Hello, {name}!'})
