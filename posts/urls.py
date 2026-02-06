from django.contrib import admin
from django.urls import path, include
from posts.views import *

urlpatterns = [
    #path('', hello_world, name = 'hello_world'),
    #path('page', index, name='my-page'),
    #path('<int:id>', get_post_detail)

    path('', post_list, name = "post_list")
]