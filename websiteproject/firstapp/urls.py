from django.urls import path
from .views import *

#www.address.com/news/
urlpatterns = [
    path('',index, name = 'home'),
    path('about/', about, name = 'about'),
    path('contactus/', contactus, name = 'contact'),
    path('category/<int:category_id>',get_category, name = 'category'),
    path('view_news/<int:news_id>',view_news, name = 'view_news'),
    path('view_news/add-news',add_news, name = 'add_news')
]

