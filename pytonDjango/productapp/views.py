from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.utils import timezone
from .models import Blogs
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password

# Create your views here.
def index_page(request):
    return render(request, "productapp/index.html")

def loginPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username = username).exists():
            messages.warning(request, "Invalid username.")
            return redirect('')
        
        user = authenticate(request,username = username, password = password)
        if user is None:
            messages.warning(request, "Invalid password.")
            return redirect('')
        
        else:
            login(request, user)
            return redirect('/myblogs')

    return render(request, "productapp/login.html")

def render_signup_view(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(username = username)
        salt = "qfB8ByKjW0or4MBvxn2Omu"
        userPwd = make_password(password, salt=salt)
        print(userPwd,"userPwd")
        if user.exists():
            messages.warning(request, "Username already exists.")
            return redirect('/signup')
        
        user = User.objects.create(

            first_name = first_name,
            last_name = last_name,
            username = username,
        
        )
        user.set_password(password)
        
        user.save()
        messages.warning(request, "Account created successfuly!.")

    return render(request, "productapp/signup.html")

def logout_page(request):
    logout(request)
    return redirect('/')

@login_required(login_url='/')
def render_myblog_view(request):
    queryset = Blogs.objects.filter(user_id = request.user)
    context = {'blogs': queryset}
    return render(request, "productapp/my-blogs.html", context)

@login_required(login_url='/')
def render_addblog_view(request):
    if request.method == "POST":
        files_data = request.FILES
        user = User.objects.get(username=request.user)

        title = request.POST.get('title')
        image = files_data.get('image')
        content = request.POST.get('content')
        publication_date = timezone.now()

        blog = Blogs.objects.create(
            user = user,
            title = title,
            image = image,
            content = content,
            publication_date = publication_date,
        )
        
        blog.save()
        messages.warning(request, "Blog created successfuly!.")
        return redirect('render_myblog_view')

    return render(request, "productapp/add_blog.html")

@login_required(login_url='/')
def delete_blog(request, id):
    queryset = Blogs.objects.get(id=id)
    queryset.delete()
    messages.warning(request, "Blog deleted successfuly!.")
    return redirect('render_myblog_view')

@login_required(login_url='/')
def blog_details(request, id):
    queryset = Blogs.objects.get(id=id)
    context = {'blog': queryset}
    return render(request, "productapp/blog-details.html", context)

@login_required(login_url='/')
def edit_blog(request, id):
    queryset = Blogs.objects.get(id=id)

    if request.method == "POST":
        files_data = request.FILES
        user = User.objects.get(username=request.user)

        title = request.POST.get('title')
        image = files_data.get('image')
        content = request.POST.get('content')
        publication_date = timezone.now()

        queryset.title = title
        if image:
            queryset.image = image
        queryset.content = content
        queryset.publication_date = publication_date

        queryset.save()
        messages.warning(request, "Blog updated successfuly!.")
        return redirect('render_myblog_view')

    context = {'blog': queryset}
    return render(request, "productapp/update-blog.html", context)
