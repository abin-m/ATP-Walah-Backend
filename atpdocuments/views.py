
from .models import ATPDocument, ATPDocumentDetails
from .serializers import ATPDocumentSerializer, ATPDocumentDetailsSerializer
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from .serializers import UserRegistrationSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token

class ATPDocumentListCreateView(generics.ListCreateAPIView):
    queryset = ATPDocument.objects.all()
    serializer_class = ATPDocumentSerializer
    permission_classes = [permissions.IsAuthenticated]

class ATPDocumentDetailsListCreateView(generics.ListCreateAPIView):
    queryset = ATPDocumentDetails.objects.all()
    serializer_class = ATPDocumentDetailsSerializer
    permission_classes = [permissions.IsAuthenticated]


class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        user = serializer.save()
        Token.objects.create(user=user)


# class CustomObtainAuthToken(ObtainAuthToken):
#     def post(self, request, *args, **kwargs):
#         response = super().post(request, *args, **kwargs)
#         token, created = Token.objects.get_or_create(user=request.user)
#         return Response({'token': token.key, 'username': request.user.username})

