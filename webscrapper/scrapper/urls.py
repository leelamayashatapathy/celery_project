from django.urls import path
from .views import index,run_scrappr

urlpatterns = [
    path('', index ,name='home'),
    path('run_scraper/', run_scrappr ,name='run_scraper'),
    
    
]