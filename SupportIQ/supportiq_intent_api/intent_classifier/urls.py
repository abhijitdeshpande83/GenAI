from django.urls import path
from .views import index, intent_classify

urlpatterns = [
    path('', index, name='index'),
    path('intent_classify/', intent_classify, name='intent_classify')
]