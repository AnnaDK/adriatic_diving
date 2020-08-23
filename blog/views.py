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
    comments = Comment.objects.filter(created_date__lte=timezone.now()
           ).order_by('-created_date') 
    newcomment = None 
    if request.method == "POST":
        form = BlogCommentForm(data=request.POST)
        if form.is_valid():
            newcomment = form.save(commit=False)
            newcomment.post = post
            newcomment.save()
            form.save()
            return redirect(single_post, post.id)
            
    else:
        form = BlogCommentForm()

    return render(request, "post.html", {'post': post, 'form': form, 'comments': comments, 'newcomment': newcomment })

  
def edit_comment(request, pk):
    """
    Create a view that allows us to create
    or edit a post depending if the Post ID
    is null or not
    """
    comment = get_object_or_404(Comment, pk=pk)
    if request.method == "POST":
        form = BlogCommentForm(request.POST, request.FILES, instance=comment)
        if form.is_valid():
            post = form.save()
            return redirect('post', post.pk)
    else:
        form = BlogCommentForm(instance=comment)
    return render(request, 'post.html', {'form': form})