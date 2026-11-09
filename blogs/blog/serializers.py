from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    author_name = serializers.ReadOnlyField(source='author.username')
    image = serializers.ImageField(required=False, allow_null=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'image', 'author_name', 'created_at']