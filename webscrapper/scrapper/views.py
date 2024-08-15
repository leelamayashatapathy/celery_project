from django.shortcuts import render
from django.http import JsonResponse
from .scripts import scrape_imdb_news
from .models import ImdbNews


from . tasks import add

def run_scrappr(request):
    scrape_imdb_news()
    return JsonResponse({
        "status":True,
        "message": "Scrapper Executed"
    })
    
    
def index(request):
    return render(request,'index.html',context={"all_news":ImdbNews.objects.all()})
