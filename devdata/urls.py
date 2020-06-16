from django.urls import path
from . import views

app_name = 'devdata'

urlpatterns = [
    path('',views.index,name='index'),
    path('blog',views.blog,name='blog'),
    path('about',views.aboutpage,name='about'),
    path('contactPage',views.contactpage,name='contactPage'),
    path('elements',views.elements,name='elements'),
    path('main',views.main,name='main'),
    path('portfolioPage',views.portfoliopage,name='portfolioPage'),
    path('portfolioDetails',views.portfolio_details,name='portfolioDetails'),
    path('service',views.services,name='service'),
    path('single_blog',views.single_blog,name='single_blog'),
]