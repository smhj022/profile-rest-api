from rest_framework import filters, status, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.settings import api_settings
from rest_framework.views import APIView

from .models import ProfileFeedItem, UserProfile
from .permission import UpdateOwnProfile, UpdateOwnStatus
from .serializers import (HelloSerializer, UserProfileFeedSerializer,
                          UserProfileSerializer)

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

    # filter functionality now user can search other user with name and email
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email')


class UserLoginApiView(ObtainAuthToken):
    """Handle creating user authentication token"""
    # it obtain auth token view , which will enable it in the django admin/
    # the rest of the view sets sand other things provided by the django
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class UserProfileFeedApiViewSet(viewsets.ModelViewSet):
    """Handles Creating Updating and Reading Profile Feed Item"""

    serializer_class = UserProfileFeedSerializer
    queryset = ProfileFeedItem.objects.all()

    # check for user authentication
    authentication_classes = (TokenAuthentication,)

    # list out the permission for the authentication user
    permission_classes = (
        UpdateOwnStatus,
        IsAuthenticatedOrReadOnly,
    )

    # perform create function override the create function
    # When a request is made to over viewset then it passed over the serializer
    # class and validate then serializer.save function is called by default
    # if we want to customize the logic for creating an object then it can be done
    # by perform create function

    def perform_create(self, serializer):
        """Sets the user profile to logged in profile"""
        serializer.save(user_profile=self.request.user)
