# blog/views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import Post  # Import the Post model only
from django.contrib.auth.decorators import login_required

def post_list(request):
    posts = Post.objects.all().order_by('-created_at')  # Correctly reference the Post model
    return render(request, 'blog/post_list.html', {'posts': posts})

@login_required
def post_create(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        Post.objects.create(title=title, content=content, author=request.user)
        return redirect('post_list')  # Redirect to post_list after creating a post
    return render(request, 'blog/post_create.html')  # Corrected template name
