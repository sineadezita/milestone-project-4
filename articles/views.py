from django.shortcuts import render, get_object_or_404
from .models import Article, Category

# Create your views here.

def article_list(request):
    """A view to show all published articles"""
    articles = Article.objects.filter(is_published=True)
    categories = Category.objects.all()

    # Category filter
    category_slug = request.GET.get('category')
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        articles = articles.filter(category=category)
    
    # Search
    query = request.GET.get('q')
    if query:
        articles = articles.filter(title__icontains=query)

    context = {
        'articles': articles,
        'categories': categories,
    }
    return render(request, 'articles/article_list.html', context)

def article_detail(request, slug):
    """ A view to show an individual article """
    article = get_object_or_404(Article, slug=slug, is_published=True)

    context = {
        'article': article,
    }
    return render(request, 'articles/article_detail.html', context)
