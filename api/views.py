# from xml.etree.ElementTree import Comment  # @CHANGE
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions

from api.models import Post, Comment
from .serializers import CommentSerializer, PostSerializer, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    #REQUISITO: AUTENTICAZIONE
    permission_classes = [permissions.IsAuthenticated]  # @CHANGE


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-date_created')
    serializer_class = PostSerializer
    #REQUISITO: AUTENTICAZIONE
    permission_classes = [permissions.IsAuthenticated]


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-date_created')
    serializer_class = CommentSerializer
    #REQUISITO: AUTENTICAZIONE
    permission_classes = [permissions.IsAuthenticated]
