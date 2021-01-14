from django.urls import path
from .views import home, post_detail, postComment, CreatePost, PostSearchView, PostLike, CommentLike, contact_us, subscribe_view

app_name = 'home'

urlpatterns = [
    path('', home, name='home'),
    path('post/new/', CreatePost, name='create_post'),
    path('post/detail/<int:pk>/', post_detail, name='post_detail'),
    path('post/postComment/', postComment, name='postComment'),
    path('post/search/', PostSearchView.as_view(), name='search_result'),
    path('post-like/<int:pk>/', PostLike, name="like_post"),
    path('comment-like/<int:pk>/', CommentLike, name="like_comment"),
    path('contact-us/', contact_us, name='contact_us'),
    path('subscribe/new/', subscribe_view, name='subscribe'),
]
