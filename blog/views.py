from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.utils import timezone
from .models import Post


def blog(request):
    posts = Post.objects.filter(created_date__lte=timezone.now()
        ).order_by('-created_date')
    
    return render(request, "blogposts.html", {'posts': posts})
    


def single_post(request, pk):
    
    post = get_object_or_404(Post, pk=pk)
    post.views += 1
    post.save()

    
    return render(request, "post.html", {'post': post})