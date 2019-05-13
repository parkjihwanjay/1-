from django.shortcuts import render, redirect
from .forms import PostForm, UserForm
from .models import Post
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            auth.login(request, new_user)
            return redirect('home')
        else:
            form = UserForm()
            error = "아이디가 이미 존재한다"
            return render(request, 'registration/signup.html', {'form':form, 'error' : error})
    else:
        form = UserForm()
        return render(request, 'registration/signup.html', {'form': form})
def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts':posts})

@login_required
def new(request):
    if request.method == 'POST':                            #글 등록
        form = PostForm(request.POST)
        post = form.save(commit=False)
        post.author=request.user.get_username() 
        post.save()
        return redirect('detail', post_pk=post.pk)
    else:                                                   #페이지 이동
        form = PostForm()
    return render(request, 'new.html', {'form': form})

def detail(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    return render(request, 'detail.html', {'post':post})

@login_required
def edit(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance = post)
        form.save()
        return redirect('detail', post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'edit.html', {'form':form})

@login_required
def delete(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    post.delete()
    return redirect('home')

