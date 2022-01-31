from django.urls import path
from .views import *

urlpatterns = [
    path('main/', MainPageView.as_view(), name='main'),
    path('all-articles/', AllArticlesPageView.as_view(), name='all'),
    path('advices/', AdvisesPageView.as_view(), name='advises'),
    path('category/<int:pk>/', CategoryArticlePageView.as_view(), name='category'),
    path('article/<int:pk>/', TheArticlePageView.as_view(), name='article'),
    path('reviews/', ReviewsPageView.as_view(), name='reviews'),
    path('contact/', ContactPageView.as_view(), name='contact'),

    path('all-category/', ChooseCategoryPageView.as_view(), name='all-category'),
    path('services/', ServicesPageView.as_view(), name='services')
]