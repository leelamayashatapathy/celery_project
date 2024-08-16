import requests
from celery import shared_task
from .models import NewsArticle
from django.utils import timezone
from celery import signals
from django_celery_beat.models import PeriodicTask, IntervalSchedule

# 'source': 'bbc-news',
# 'country': 'us',
@shared_task
def fetch_latest_news():
    url = 'https://newsapi.org/v2/everything'
    params = {
        'apiKey': '07c7199e14db4a35b42e0a4bd4fb2db4',
        'q': 'technology',
        'language': 'en',
        'sortBy': 'publishedAt',
        'pageSize': 10,
        
    }
    response = requests.get(url,params=params)
    articles = response.json().get('articles',[])
    
    for article in articles:
        image_url = article.get('urlToImage',None)
        NewsArticle.objects.create(
            title=article['title'],
            description = article['description'],
            source=article['source']['name'],
            url=article['url'],
            image = image_url,
            published_at=article['publishedAt']
        )

    print(f"Fetched {len(articles)} articles at {timezone.now()}")




@signals.setup_logging.connect
def setup_periodic_tasks(sender, **kwargs):
    # Set up a schedule to run every hour
    schedule, created = IntervalSchedule.objects.get_or_create(
        every=1,
        period=IntervalSchedule.MINUTES,
    )

    # Create the periodic task if it doesn't exist
    PeriodicTask.objects.get_or_create(
        interval=schedule,
        name='Fetch latest news every hour',
        task='aggregator.tasks.fetch_latest_news',
    )