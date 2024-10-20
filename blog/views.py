from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect 
from .models import Post, blog  
from django.contrib.auth.decorators import login_required 
def post_list(request):
    posts =posts.objects.all().order_by('-created_at')
    return render(request, 'blog/post_list.html', {'posts': posts})
# Create your views here.
@login_required
def post_create (request):
    if request.method =='POST':
        title =request.POST['title']
        content =request.POST['content']
        Post.objects.create(title=title, content=content, author=request.user)
        return redirect('post_list')
    return render (request,'blog/post_ceate.html')