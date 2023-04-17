from django.shortcuts import render
from rest_framework import viewsets, status
from django.contrib.auth.models import User
from .serializers import UserSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
# from rest_framework.response import responses
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny, )

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def viewuser(r):
    tokenn = r.headers["Authorization"][6:]
    # print(tokenn)
    queryset = Token.objects.get(key = tokenn).user_id    
    username = User.objects.get(id = queryset).username

    response = {'message' : 'you are authenticated', 'username': username}
    return Response(response, status= status.HTTP_200_OK)