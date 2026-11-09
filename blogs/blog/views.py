from django.views.generic import TemplateView
from rest_framework import generics, permissions
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from .models import Post
from .serializers import PostSerializer

class IndexView(TemplateView):
    template_name = 'index.html'

class PostListCreateAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    parser_classes = [MultiPartParser, FormParser, JSONParser] # Enables file uploads

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)