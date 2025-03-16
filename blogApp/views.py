from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .models import Post

"""
The request parameters is required by all views.
"""
def post_list(request):
    posts = Post.published.all()

    print(posts)

    return render(
        request,
        'blog/post/list.html',
        {'posts': posts}
    )

def post_detail(request, year, month, day, post):
    """
    try:
        post = Post.published.get(id=id)
    except Post.DoesNotExist:
        raise Http404("No Post found.")
    """

    post = get_object_or_404(
        Post,
        status=Post.Status.PUBLISHED,
        slug=post,
        publish__year=year,
        publish__month=month,
        publish__day=day
    )

    return render(
        request,
        'blog/post/detail.html',
        {'post': post}
    )
