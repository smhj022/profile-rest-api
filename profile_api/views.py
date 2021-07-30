from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.


class helloApiView(APIView):

    def get(self, request, format=None):
        """Return a list of APIview feature"""
        an_apiview = [
            'Uses HTTP method as function (get, post, patch, put, delete)',
            'Is similar to a traditional django view',
            'Gives you the most control over your application views',
            'Is mapped manually to URLs',
        ]

        return Response({'message': 'Hello', 'an_apiview': an_apiview})