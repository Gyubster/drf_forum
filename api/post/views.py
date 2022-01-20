from rest_framework                 import generics, status
from rest_framework.permissions     import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response        import Response

from .serializers import CommentSerializer, PostCreateSerializer, PostDetailSerializer, PostListSerializer
from post.models  import Post, Comment

class PostCreate(generics.CreateAPIView):
    queryset            = Post.objects.all()
    serializer_class    = PostCreateSerializer
    permission_classes  = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = PostCreateSerializer(data=request.data)

        if serializer.is_valid():
            post = Post.objects.create(
                    user_id    = request.user.id,
                    title      = request.data['title'],
                    content    = request.data['content'],
                    view_count = 0,
                    )
        
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset            = Post.objects.all()
    serializer_class    = PostDetailSerializer
    permission_classes  = [IsAuthenticatedOrReadOnly]

class PostList(generics.ListAPIView):
    queryset            = Post.objects.all()
    serializer_class    = PostListSerializer
    permission_classes  = [AllowAny]

class CommentCreate(generics.CreateAPIView):
    queryset            = Comment.objects.all()
    serializer_class    = CommentSerializer
    permission_classes  = [IsAuthenticatedOrReadOnly]

    def post(self, request, *args, **kwargs):
        serializer = CommentSerializer(data=request.data)

        if serializer.is_valid():
            comment = Comment.objects.create(
                        user_id = request.user.id,
                        post_id = self.kwargs['pk'],
                        content = request.data['content']
                    )
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset            = Comment.objects.all()
    serializer_class    = CommentSerializer
    permission_classes  = [IsAuthenticatedOrReadOnly]
