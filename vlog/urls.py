from django.urls import path
from vlog.views import *

urlpatterns = [
    path('', PostsListView.as_view(), name='main'),
    path('login/', Login.as_view(), name='login'),
    path('register/', UserCreateView.as_view(), name='register'),
    path('logout/', Logout.as_view(), name='logout'),
    path('create/post', PostCreateView.as_view(), name='create'),
    path('mainpost/', MainPostListView.as_view(), name='main_post'),
    path('comment/create/', CreateCommentView.as_view(), name='create_comment'),
    path('comments', CommentListView.as_view(), name='comments'),
    path('delete/post/<int:pk>', DeletePostView.as_view(), name='delete_post'),
    path('myposts/', MyPostsListView.as_view(), name='my_posts'),
]
