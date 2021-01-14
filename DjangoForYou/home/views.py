from django.shortcuts import render, HttpResponseRedirect, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count
from django.urls import reverse
from django.contrib import messages
from django.views.generic import View
from django.db.models import Q
from home.models import Post, BlogComment, Contact, Subscriber
from home.forms import PostForm


def home(request):
    post = Post.objects.all().order_by('-timeStamp')
    trending_post = Post.objects.annotate(like_count=Count('likes')).order_by('-like_count')[0:3]
    page = request.GET.get('page')
    paginator = Paginator(post, 3)
    try:
        post = paginator.page(page)
    except PageNotAnInteger:
        post = paginator.page(1)
    except EmptyPage:
        post = paginator.page(paginator.num_pages)
    context = {
        'post': post,
        'trending_post': trending_post,
    }
    return render(request, 'home/home.html', context)


def CreatePost(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author_name = request.user
            instance.save()
            messages.success(request, "Posted Successfully Article")
            return redirect('home:post_detail', instance.id)
    else:
        form = PostForm()
    context = {
        'form': form
    }
    return render(request, 'home/create_post.html', context)


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    trending_post = Post.objects.annotate(like_count=Count('likes')).order_by('-like_count')[0:3]
    comments = BlogComment.objects.filter(post=post)
    print(comments)
    context = {
        'post': post,
        'comments': comments,
        'user': request.user,
        'trending_post': trending_post
    }
    return render(request, 'home/post_detail.html', context)


def postComment(request):
    if request.method == 'POST':
        body = request.POST.get('comment')
        user = request.user
        post_pk = request.POST.get('post_pk')
        post_comment = Post.objects.get(id=post_pk)
        if post_comment:
            comment = BlogComment(body=body, user=user, post=post_comment)
            comment.save()
            messages.success(request, "Successfully posted reply comment")
    return redirect(f"/post/detail/{post_comment.pk}")


class PostSearchView(View):
    def get(self, *args, **kwargs):
        queryset = Post.objects.all()
        query = self.request.GET['query']
        trending_post = Post.objects.annotate(like_count=Count('likes')).order_by('-like_count')[0:3]
        result = queryset.filter(
            Q(title__icontains=query) | Q(body__icontains=query)
        )
        context = {
            'post': result,
            'query': query,
            'trending_post': trending_post
        }
        return render(self.request, 'home/search_result.html', context)
    

def PostLike(request, pk):
    if request.method == 'POST':
        post = get_object_or_404(Post, id=request.POST.get('post_id'))
        liked = False
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
            liked = False
        else:
            post.likes.add(request.user)
            liked = True
    return HttpResponseRedirect(reverse('home:post_detail', args=[str(pk)]))


def CommentLike(request, pk):
    if request.method == 'POST':
        comment = get_object_or_404(BlogComment, id=request.POST.get('comment_id'))
        post_id = get_object_or_404(Post, id=request.POST.get('post_id'))
        liked = False
        if comment.likes.filter(id=request.user.id).exists():
            comment.likes.remove(request.user)
            liked = False
        else:
            comment.likes.add(request.user)
            liked = True
    return redirect(f"/post/detail/{post_id.id}")


def contact_us(request):
    if request.method == 'POST':
        name  =  request.POST.get('name')
        email =  request.POST.get('emailadd')
        phone =  request.POST.get('phone')
        body  =  request.POST.get('body')
        contact = Contact(
            name=name,
            email=email,
            phone=phone,
            body=body,   
        )
        contact.save()
        return redirect('/')
    return render(request, 'home/contact.html')


def subscribe_view(request):
    if request.method == 'POST':
        sub = Subscriber(email=request.POST['email'])
        sub.save()
    return redirect('/')