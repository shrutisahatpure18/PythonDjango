from django.urls import path, include
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    # path('login', index, name='index')
    path('admin-panel', index_page, name='index_page'),
    path('blog-list', blog_list, name='blog_list'),
    path('deactivate-user/<int:user_id>/', deactivate_user, name='deactivate_user'),
    path('activate-user/<int:user_id>/', activate_user, name='activate_user'),
]