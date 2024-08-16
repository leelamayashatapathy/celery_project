from django.http import JsonResponse
from .models import NewsArticle

def latest_news(request):
    articles = NewsArticle.objects.all().order_by('-published_at')[:10]
    data = [{"title": article.title, "source": article.source, "url": article.url} for article in articles]
    return JsonResponse(data, safe=False)
