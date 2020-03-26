
from django.urls import path
from .views import news,details

urlpatterns = [
    
    path('',news,name='news'),
    path('details/<int:id>',details, name='detail'),
    
    
]