from django.shortcuts import render
from .models import Post,Comments
from .forms import CommentForm
from django.contrib import messages
from django.utils import timezone
from django.db.models import Q
from django.core.paginator import Paginator
# Create your views here.

def blog_list(request):
    blogs_list=Post.objects.all()
    paginator=Paginator(blogs_list,3)
    page = request.GET.get('page')
    blogs = paginator.get_page(page)
    search_query=request.GET.get('q')
    if search_query:
        blogs=blogs.filter(
            Q(title__icontains = search_query)|
            Q(content__icontains = search_query)
        )
    context={
        'blogs':blogs,
    }
    return render(request,'blog/blog_list.html',context)


def blog_detail(request,num):
    blog_detail=Post.objects.get(id=num)
    comments_list=Comments.objects.filter(post=blog_detail)
    context={
        'blog_detail':blog_detail,
        'comments':comments_list
    }
    if request.method == 'POST':
        newform=CommentForm(request.POST,request.FILES)
        if newform.is_valid():
            new_comment=newform.save(commit=False)
            new_comment.post=blog_detail
            new_comment.save()
            messages.success(request,'Thanks for your feedback')
            return render(request, 'blog/blog_details.html', context)
        else:
            messages.success(request,('There is a problem please try again '))
            return render(request, 'blog/blog_details.html', context)
    else:
        return render(request, 'blog/blog_details.html', context)