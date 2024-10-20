from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from django.contrib.auth.decorators import login_required 

def post_list(request):
    posts = Post.objects.all().order_by('-created_at')  # Corrected to use Post model
    return render(request, 'blog/post_list.html', {'posts': posts})

@login_required
def post_create(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        Post.objects.create(title=title, content=content, author=request.user)
        return redirect('post_list')
    return render(request, 'blog/post_create.html')  # Fixed typo in template name
