from rest_framework import viewsets
from rest_framework.response import Response

from core.serializers import PostSerializer
from core.models import Post


class PostViewSet(viewsets.ModelViewSet):
    serialiser_class = PostSerializer
    queryset = Post.objects.all()
    lookup_field = 'slug'
