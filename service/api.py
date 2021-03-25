from rest_framework.views import APIView
from rest_framework.response import Response


class Hello1API(APIView):
    def get(self, request, format=None):
        name = request.query_params.get('name')
        return Response({'response': f'Hello, {name}!'})


class Hello2API(APIView):
    def get(self, request, format=None, **kwargs):
        name = kwargs['name']
        return Response({'response': f'Hello, {name}!'})
