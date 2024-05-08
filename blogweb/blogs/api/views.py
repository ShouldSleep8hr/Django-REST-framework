
from django.shortcuts import get_object_or_404
from blogs.models import Tag, Blog, Comment
from rest_framework import generics, serializers
from .serializers import TagSerializer, BlogSerializer, CommentSerializer

import requests

from rest_framework.response import Response
from rest_framework import status

from blogs.permission import IsAuthenticated, IsOwner
from rest_framework.permissions import IsAdminUser

class TagListAPI(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class BlogTagAPI(generics.ListCreateAPIView):
    serializer_class = BlogSerializer

    def get_queryset(self):
        queryset = Blog.objects.all()
        tag_id = self.kwargs['pk']
        tag = Tag.objects.get(pk=tag_id)
        queryset = queryset.filter(tag=tag)
        return queryset

class TagCreateAPI(generics.CreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsAdminUser]

class TagUpdateAPI(generics.UpdateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsAdminUser]

class TagDeleteAPI(generics.DestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsAdminUser]


class BlogListAPI(generics.ListAPIView):
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
        # Assign tag if provided in request data
        tag_id = int(self.request.data.get('tag'))
        tag_instance = Tag.objects.get(pk=tag_id)
        # Set the user as the one who is logged in
        serializer.save(user=self.request.user, tag=tag_instance)

        # Send Line notification
        message = f'New blog post created by {self.request.user.username}!'
        access_token = 'e6VMEXjkpFmQi8HdsSeLieGo2QNf4h6muQjmIO0QxuE'
        self.send_line_notification(message, access_token)

    def send_line_notification(self, message, access_token):
        url = 'https://notify-api.line.me/api/notify'
        headers = {'Authorization': f'Bearer {access_token}'}
        data = {'message': message}
        response = requests.post(url, headers=headers, data=data)
        if response.status_code == 200:
            print('Notification sent successfully')
        else:
            print(f'Failed to send notification. Status code: {response.status_code}')


class BlogUpdateAPI(generics.UpdateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsAdminUser | IsOwner]

    def perform_update(self, serializer):
        # Assign tag if provided in request data
        tag_id = int(self.request.data.get('tag'))
        tag_instance = Tag.objects.get(pk=tag_id)
        # Set the user as the one who is logged in
        serializer.save(tag=tag_instance)

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