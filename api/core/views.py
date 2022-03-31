from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response

from core.serializers import PostSerializer
from core.models import Post


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'slug'
    permission_classes = [permissions.AllowAny]
