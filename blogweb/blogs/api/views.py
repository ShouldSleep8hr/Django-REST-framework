

from django.shortcuts import get_object_or_404
from blogs.models import Blog, Comment
from rest_framework import generics
from .serializers import TagSerializer, BlogSerializer, CommentSerializer

from blogs.permission import IsAuthenticated, IsOwner
from rest_framework.permissions import IsAdminUser

class BlogListAPI(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class BlogDetailAPI(generics.RetrieveAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class BlogCreateAPI(generics.CreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Set the user as the one who is logged in
        serializer.save(user=self.request.user)

class BlogUpdateAPI(generics.UpdateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsAdminUser | IsOwner]

class BlogDeleteAPI(generics.DestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsAdminUser | IsOwner]



class CommentListAPI(generics.ListCreateAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        # Get the primary key (pk) from the URL kwargs
        pk = self.kwargs.get('pk')
        # Filter the queryset to get comments for the specified pk
        return Comment.objects.filter(blog=pk)

class CommentCreateAPI(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Get the blog instance corresponding to the provided primary key
        blog = get_object_or_404(Blog, pk=self.kwargs['pk'])
        serializer.save(user=self.request.user, blog=blog)
            
class CommentUpdateAPI(generics.UpdateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAdminUser | IsOwner]

class CommentDeleteAPI(generics.DestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAdminUser | IsOwner]