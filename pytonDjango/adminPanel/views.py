from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.http import JsonResponse

from productapp.models import Blogs

def deactivate_user(request, user_id):
    # Retrieve the user object
    user = User.objects.get(id=user_id)
    
    # Deactivate the user account
    user.is_active = False
    user.save()
    
    return redirect('/admin-panel')  # Redirect to the user listing page after deactivation

def activate_user(request, user_id):
    # Retrieve the user object
    user = User.objects.get(id=user_id)
    
    # Activate the user account
    user.is_active = True
    user.save()
    
    return redirect('/admin-panel')  # Redirect to the user listing page after activation

def index_page(request):
    # Get sorting parameter from the request
    sort_by = request.GET.get('sort_by', 'username')  # Default sorting by username
    
    # Retrieve users queryset based on sorting parameter
    if sort_by == 'name':
        users = User.objects.all().order_by('first_name', 'last_name')
    elif sort_by == 'status':
        users = User.objects.all().order_by('active')
    else:
        users = User.objects.all().order_by('username')
    
    # Apply search functionality
    query = request.GET.get('q', '')
    if query:
        users = users.filter(username__icontains=query)
    paginator = Paginator(users, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'adminPanel/index.html', {'page_obj': page_obj, 'sort_by': sort_by})


def blog_list(request):
    # Get sorting parameter from the request
    sort_by = request.GET.get('sort_by', 'title')  # Default sorting by username
    blogs = Blogs.objects.all()
    # # Retrieve users queryset based on sorting parameter
    # if sort_by == 'name':
    #     users = User.objects.all().order_by('first_name', 'last_name')
    # elif sort_by == 'status':
    #     users = User.objects.all().order_by('active')
    # else:
    #     users = User.objects.all().order_by('username')
    
    # Apply search functionality
    query = request.GET.get('q', '')
    if query:
        blogs = blogs.filter(title__icontains=query)
    paginator = Paginator(blogs, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'adminPanel/blog-list.html', {'page_obj': page_obj, 'sort_by': sort_by})
