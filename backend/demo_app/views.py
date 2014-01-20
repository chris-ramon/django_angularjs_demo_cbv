from demo_app.models import Post
from demo_app.serializers import PostSerializer
from rest_framework import generics


class PostList(generics.ListCreateAPIView):
    paginate_by = 1
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer