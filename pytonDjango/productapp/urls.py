from django.urls import path, include
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    # path('login', index, name='index')
    path('', loginPage, name='loginPage'),
    # path('loginPage', loginPage, name='loginPage'),
    
    path('signup', render_signup_view, name='render_signup_view'),
    path('myblogs', render_myblog_view, name='render_myblog_view'),
    path('addblogs', render_addblog_view, name='render_addblog_view'),
    path('delete-blog/<id>', delete_blog, name='delete_blog'),
    path('blog-details/<id>', blog_details, name='blog_details'),
    path('edit-blog/<id>', edit_blog, name='edit_blog'),
    path('logout', logout_page, name='logout_page'),
    # path('student_form', student_form, name='student_form'),
]