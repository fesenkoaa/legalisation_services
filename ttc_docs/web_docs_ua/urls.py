from django.urls import path
from .views import *

urlpatterns = [
    path('main/', UaMainPageView.as_view(), name='main'),
    path('all-articles/', UaAllArticlesPageView.as_view(), name='all'),
    path('advices/', UaAdvisesPageView.as_view(), name='advises'),
    path('category/<int:pk>/', UaCategoryArticlePageView.as_view(), name='category'),
    path('article/<int:pk>/', UaTheArticlePageView.as_view(), name='article'),
    path('reviews/', UaReviewsPageView.as_view(), name='reviews'),
    path('contact/', UaContactPageView.as_view(), name='contact'),

    path('all-category/', UaChooseCategoryPageView.as_view(), name='all-category'),
    path('services/', UaServicesPageView.as_view(), name='services')

]