from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from .models import Post, Category


def index(request):
    """Главная страница - пять последних публикаций."""
    post_list = Post.objects.filter(
        is_published=True,
        category__is_published=True,
        pub_date__lte=timezone.now()
    ).order_by('-pub_date')[:5]
    context = {'post_list': post_list}
    return render(request, 'blog/index.html', context)


def post_detail(request, post_id):
    """Страница отдельной публикации."""
    post = get_object_or_404(
        Post,
        pk=post_id,
        is_published=True,
        category__is_published=True,
        pub_date__lte=timezone.now()
    )
    context = {'post': post}
    return render(request, 'blog/post_detail.html', context)


def category_posts(request, category_slug):
    """Страница категории."""
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True
    )
    post_list = Post.objects.filter(
        category=category,
        is_published=True,
        pub_date__lte=timezone.now()
    ).order_by('-pub_date')
    context = {'category': category, 'post_list': post_list}
    return render(request, 'blog/category.html', context)
