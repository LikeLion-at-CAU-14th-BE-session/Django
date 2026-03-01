from django.contrib import admin
from django.urls import path, include
from posts.views import *

urlpatterns = [
    #path('', hello_world, name = 'hello_world'),
    #path('page', index, name='my-page'),
    #path('<int:id>', get_post_detail)

   # path('', post_list, name = "post_list"), # Post 생성, 전체조회
   # path('<int:post_id>/', post_detail, name = "post_detail"), # Post 단일조회, 수정, 삭제

    path('', PostList.as_view()), # DRF - 전체
    path('<int:post_id>/', PostDetail.as_view()), #DRF - 상세

    # path('comment/', comment_list, name = "comment_list"), # Comment 생성
    # path('<int:post_id>/comment/', comments_in_posts, name = "comments_in_posts"), # post 별 Comment 조회

    path('comment/', CommentList.as_view()), # DRF 과제 - Comment 생성
    path('<int:post_id>/comment/', CommentsInPosts.as_view()), # DRF 과제 - post Comment 조회
    path('comment/<int:comment_id>/', CommentDetail.as_view()), # DRF 과제 - comment 삭제

    path('category/<int:category_id>/', posts_in_category, name = "posts_in_category") # category 별 post 조회

]