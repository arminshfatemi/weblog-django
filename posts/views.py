from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from .forms import CommentForm, PostForm
from django.http import Http404


def home(request):
    posts = Post.objects.filter(hidden=False).order_by('created_time')[:8]
    context = {'posts': posts}
    return render(request, 'posts/homepage.html', context=context)


def post_detail(request, pk):
    try:
        post = get_object_or_404(Post, pk=pk)

    except Http404:
        return render(request, 'posts/notfound404.html')

    comments = Comment.objects.filter(post=post).all()

    # except:
    # comment = None
    context = {'post': post, 'comments': comments}
    return render(request, 'posts/postdetail.html', context=context)


def about(request):
    post = Post.objects.all()
    context = {'posts': post}
    return render(request, 'posts/about.html', context)


def allpost(request):
    posts = Post.objects.filter(hidden=False).order_by('created_time')
    context = {'posts': posts}
    return render(request, 'posts/allpost.html', context=context)


def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            Post.objects.create(**form.cleaned_data)
            return redirect('/allpost/', )

    else:
        form = PostForm()

    return render(request, 'posts/post_create.html', {'form': form})


def create_comment(request, pk):
    print(pk)
    post = Post.objects.get(id=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        print(post)
        if form.is_valid():
            Comment.objects.create(post=post, **form.cleaned_data)
            return redirect(f'/allpost/{pk}')

    else:
        form = CommentForm()
    # 'post': post,
    return render(request, 'posts/commentcreate.html', {'form': form, 'post': post, 'pk': pk})
