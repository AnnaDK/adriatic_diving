from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.utils import timezone
from .models import Post, Comment
from .forms import BlogCommentForm


def our_blog(request):
    posts = Post.objects.filter(created_date__lte=timezone.now()
        ).order_by('-created_date')
    
    return render(request, "blogposts.html", {'posts': posts})
    


def single_post(request, pk):
    
    post = get_object_or_404(Post, pk=pk)
    post.views += 1
    post.save()

    
    return render(request, "post.html", {'post': post})




def create_or_edit_comment(request, pk=None):
    
    comment = get_object_or_404(Comment, pk=pk) if pk else None
    if request.method == "POST":
        form = BlogCommentForm(request.POST, request.FILES, instance=comment)
        if form.is_valid():
            comment = form.save()
            return redirect(single_post, comment.pk)
    else:
        form = BlogCommentForm(instance=comment)
    return render(request, 'comment.html', {'form': form, 'comment': comment})

