from django.urls import path
from .views import index, intent_classify, health

urlpatterns = [
    path('', index, name='index'),
    path('intent_classify/', intent_classify, name='intent_classify'),
    path('health', health, name='health')
]