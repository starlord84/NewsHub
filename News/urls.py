from django.urls import path
from News.views import HomeNews, NewsByCategory, ViewNews, AddNews, register, user_login, user_logout, add_comment
from django.views.decorators.cache import cache_page
from . import views
urlpatterns = [
    path('', cache_page(60)(HomeNews.as_view()), name='Home'),
    path('category/<int:category_id>/', NewsByCategory.as_view(), name='Category'),
    path('news/<int:pk>/', ViewNews.as_view(), name='View_news'),
    path('news/add_news', AddNews.as_view(), name='Add_news'),
    path('register/', register, name='Register'),
    path('login/', user_login, name='Login'),
    path('logout/', user_logout, name='Logout'),
    path('news/<int:news_id>/add_comment/', add_comment, name='add_comment'),
]

