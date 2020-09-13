from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils import timezone
from .models import BlogPost, BlogComment, BlogAdvert
from .forms import BlogCommentForm
from django.contrib import messages

# To show all blogposts from db
# filtered by created date
# show advert cards
def our_blog(request):
    posts = BlogPost.objects.filter(created_date__lte=timezone.now()
                                    ).order_by('-created_date')
    adverts = BlogAdvert.objects.all()
    paginator = Paginator(posts, 4)  # Show 5 contacts per page

    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        posts = paginator.page(paginator.num_pages)
    return render(request, "blogposts.html", {'posts': posts,
                                              'adverts': adverts})

# to show a single post
# comments will be showing only under related post
def single_post(request, pk):

    post = get_object_or_404(BlogPost, pk=pk)
    post.views += 1
    post.save()
    comments = BlogComment.objects.filter(post=post)
    newcomment = None
    if request.method == "POST":
        form = BlogCommentForm(data=request.POST)
        if form.is_valid():
            newcomment = form.save(commit=False)
            newcomment.post = post
            newcomment.save()
            form.save()
            messages.success(request, 'your comment is awaiting an approval.')
            return redirect(single_post, post.id)

    else:
        form = BlogCommentForm()

    return render(request, "post.html", {'post': post, 'form': form, 
                                         'comments': comments,
                                         'newcomment': newcomment})

