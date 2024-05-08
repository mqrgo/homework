from django.shortcuts import render, get_object_or_404
from main_board.models import NewsPost, Category

# Create your views here.
def index(request, category_slug=None):
    categories = Category.objects.all()
    posts = NewsPost.objects.all()
    if category_slug:
        posts = NewsPost.objects.filter(category__slug=category_slug)
    return render(request, 'main_board/index.html', {'posts': posts, 'categories': categories})

def detail(request, year, month, day, post_slug):
    post = get_object_or_404(
        NewsPost,
        created__year=year,
        created__month=month,
        created__day=day,
        slug=post_slug,
    )
    return render(request, 'main_board/detail.html', {'post': post})