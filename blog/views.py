from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.shortcuts import redirect, render_to_response
from .models import Post, User
from .forms import PostForm, UserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
#from django.http import *
from django.template import RequestContext

# Create your views here.
#posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')

'''
def login_user(request):
    logout(request)
    username = password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        #authenticate
        user = authenticate(user=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'blog/post_list.html')
        else:
            return render_to_response(request, 'blog/login_user.html', context_instance=RequestContext(request))
    else:
        return render_to_response(request, 'blog/login_user.html', context_instance=RequestContext(request))
'''
#@login_required
def post_list(request):
    '''
    username = request.POST['username']
    password = request.POST['password']
    # authenticate
    user = authenticate(user=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
    '''
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    post1 = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'blog/post_list.html', {'posts': posts, 'post1':post1})
    #else:
        #return render_to_response(request, 'blog/login_user.html', context_instance=RequestContext(request))

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            #post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            #post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post) #instance=post is added for edit view
    return render(request, 'blog/post_edit.html', {'form': form})

def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'blog/post_draft_list.html', {'posts': posts})

def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('blog.views.post_detail', pk=pk)

def add_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, "Thanks for registering. Please login to continue.")
            username = request.POST['username']
            password = request.POST['password']
            #authenticate
            user = authenticate(user=username, password=password)
            print(user)
            user.backend = 'django.contrib.auth.backend.ModelBackend'
            login(request, user)
            return render(request, 'blog/post_list.html', {'posts': posts})
    else:
        form = UserForm()
    return render(request, 'blog/add_user.html', {'form': form})