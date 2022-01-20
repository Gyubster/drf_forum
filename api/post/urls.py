from django.urls             import path
from django.utils.functional import unpickle_lazyobject

from .views import CommentCreate, CommentDetail, PostCreate, PostDetail, PostList

app_name = 'posts'

urlpatterns = [
        path('/create', PostCreate.as_view(), name='post-create'),
        path('/<int:pk>', PostDetail.as_view(), name='post-detail'),
        path('/<int:pk>/comments', CommentDetail.as_view(), name='post-comment'),
        path('/<int:pk>/comments/create', CommentCreate.as_view(), name='post-comment-create'),
        path('/', PostList.as_view(), name='post-list'),
        ]
