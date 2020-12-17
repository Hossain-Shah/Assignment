from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PostSerializer
from .models import Post


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('tsync_id')
    serializer_class = PostSerializer


