from django.urls import path
from .views import HomePageView, HomePageNews, HomePageNewsDetail, HomePageNewsCreate, HomePageNewsEdit, HomePageNewsDelete
urlpatterns = [
    path('',HomePageView.as_view(), name = 'home'),
    path('news/',HomePageNews.as_view(), name = 'news'),
    path('news/<uuid:pk>/',HomePageNewsDetail.as_view(), name = 'news_detail'),
    path('news/new/',HomePageNewsCreate.as_view(), name = 'news_create'),
    path('news/edit/<uuid:pk>/',HomePageNewsEdit.as_view(),name = 'news_edit'),
    path('news/delete/<uuid:pk>/',HomePageNewsDelete.as_view(), name = 'news_delete'),
]