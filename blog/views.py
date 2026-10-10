
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from .models import Post, Comment, Category


def main(request):
    return render(request, 'main.html')


def users(request):
    all_users = User.objects.all().order_by('id')
    return render(request, 'users.html', {'users': all_users})


def blogs(request):
    all_posts = Post.objects.select_related(
        'category'
    ).all().order_by('id')

    return render(request, 'blogs.html', {'posts': all_posts})


def comments(request):
    all_comments = Comment.objects.select_related(
        'post', 'user'
    ).all().order_by('id')

    return render(
        request,
        'comments.html',
        {'comments': all_comments}
    )


def categories(request):
    all_categories = Category.objects.all().order_by('id')

    return render(
        request,
        'categories.html',
        {'categories': all_categories}
    )


def blogdetails(request, id):
    post = get_object_or_404(
        Post.objects.select_related('category'),
        id=id
    )

    return render(
        request,
        'blogdetails.html',
        {'post': post}
    )