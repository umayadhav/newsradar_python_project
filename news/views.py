# news/views.py

from django.shortcuts import render, redirect
from services.news_service import NewsService
from services.search_service import SearchService
from storage.favourites import FavouritesManager
from models.digest import DailyDigest

# Initialize services (shared across all views)
news_service   = NewsService()
search_service = SearchService()
favourites     = FavouritesManager()

def home(request):
    """Home page — Top Headlines"""
    articles = news_service.fetch_top_headlines()
    articles = search_service.sort_by_latest(articles)
    return render(request, 'news/home.html', {
        'articles': articles,
        'page_title': '🌍 Top Headlines'
    })

def category(request, category):
    """Category page — Tech, Sports, Business"""
    keywords = {
        'technology': 'technology AI software',
        'sports'    : 'sports cricket IPL football',
        'business'  : 'business economy market stocks',
    }
    query    = keywords.get(category, category)
    articles = news_service.fetch_by_keyword(query)
    articles = search_service.sort_by_latest(articles)

    titles = {
        'technology': '💻 Technology News',
        'sports'    : '🏏 Sports News',
        'business'  : '💰 Business News',
    }
    return render(request, 'news/category.html', {
        'articles'  : articles,
        'page_title': titles.get(category, category.capitalize()),
        'category'  : category
    })

def search(request):
    """Search page"""
    articles = []
    keyword  = ""

    if request.method == "GET" and request.GET.get('q'):
        keyword  = request.GET.get('q', '').strip()
        articles = news_service.fetch_by_keyword(keyword)
        articles = search_service.sort_by_latest(articles)

    return render(request, 'news/search.html', {
        'articles'  : articles,
        'keyword'   : keyword,
        'page_title': '🔍 Search News'
    })

def favourites_view(request):
    """Favourites page"""
    return render(request, 'news/favourites.html', {
        'articles'  : favourites.favourites,
        'page_title': '⭐ My Favourites'
    })

def add_favourite(request):
    """Save article to favourites"""
    if request.method == "POST":
        from models.article import Article
        article = Article(
            title        = request.POST.get('title', ''),
            description  = request.POST.get('description', ''),
            url          = request.POST.get('url', ''),
            source       = request.POST.get('source', ''),
            author       = request.POST.get('author', ''),
            published_at = request.POST.get('published_at', ''),
            category     = request.POST.get('category', 'general')
        )
        favourites.add_article(article)
    return redirect(request.POST.get('next', '/'))

def remove_favourite(request, index):
    """Remove article from favourites"""
    favourites.remove_article(index)
    return redirect('favourites')

def digest(request):
    """Daily Digest page"""
    articles      = news_service.fetch_top_headlines()
    daily_digest  = DailyDigest(articles)
    return render(request, 'news/digest.html', {
        'articles'  : daily_digest.articles,
        'date'      : daily_digest.date,
        'page_title': '📋 Daily Digest'
    })

# Fix url name
favourites_view.__name__ = 'favourites'
urlpatterns_extra = None
