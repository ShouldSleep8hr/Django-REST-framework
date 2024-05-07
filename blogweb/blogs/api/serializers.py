from blogs.models import Tag, Blog, Comment
from rest_framework import serializers

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['name']

class BlogSerializer(serializers.ModelSerializer):
    tag = serializers.CharField(source='tag.name', read_only=True)
    user = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Blog
        fields = ['id', 'title_text', 'content_text', 'user', 'tag']
        read_only_fields = ['user']  # Exclude 'user' from being required during creation

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username', read_only=True)
    class Meta:
        model = Comment
        fields = ['id', 'text', 'user', 'blog']
        read_only_fields = ['user', 'blog']