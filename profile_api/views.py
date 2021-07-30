from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication


from .serializers import HelloSerializer, UserProfileSerializer
from .models import UserProfile
from .permission import UpdateOwnProfile

# Create your views here.


class helloApiView(APIView):
    """Test API View"""
    serializer_class = HelloSerializer

    def get(self, request, format=None):
        """Return a list of APIview feature"""
        an_apiview = [
            'Uses HTTP method as function (get, post, patch, put, delete)',
            'Is similar to a traditional django view',
            'Gives you the most control over your application views',
            'Is mapped manually to URLs',
        ]

        return Response({'message': 'Hello', 'an_apiview': an_apiview})

    def post(self, request):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f"Hello {name}"
            return Response({'message': message})

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def put(self, request, pk=None):
        """Handle Updating an object"""
        return Response({"method": "PUT"})

    def patch(self, request, pk=None):
        """Handle Partial Update in object"""
        return Response({"method": "PATCH"})

    def delete(self, request, pk=None):
        """Handle Delete an object"""
        return Response({"method": "DELETE"})


class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""
    serializer_class = HelloSerializer

    def list(self, request):
        """Return a Hello message"""

        a_viewset = [
            "Uses action (list, create, retrieve, update, partial_update)",
            "Automatic maps Urls using routes",
            "Provide more functionality with less code "

        ]

        return Response({"message": "Hello", "viewset": a_viewset})

    def create(self, request):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f"Hello {name}!!"
            return Response({'message': message})

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def retrive(self, request, pk=None):
        """Handle getting an object by id"""
        return Response({"Http_method": "GET"})

    def update(self, request, pk=None):
        """Handle Updating an object"""
        return Response({"Http_method": "PUT"})

    def partial_update(self, request, pk=None):
        """Handle updating partially an object"""
        return Response({"Http_method": "PATCH"})

    def destroy(self, request, pk=None):
        """Handle delete an object"""
        return Response({"Http_method": "DELETE"})


class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()

    # check for user authentication
    authentication_classes = (TokenAuthentication,)

    # list out the permission for the authentication user
    permission_classes = (UpdateOwnProfile,)

