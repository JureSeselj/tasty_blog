from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from .forms import CommentForm
from .views import *

urlpatterns = [
    path('', views.index, name="index"),
    path('search/', views.search, name="search"),
    path('about/', views.about, name="about"),
    path('blog/', views.BlogPost.as_view(), name="blog"),
    path('contact/', views.contact, name="contact"),
    path('categories/', views.categories, name="categories"),
    path('categories_posts/<str:cats>', views.CategoriesView, name="categories_posts"),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),

]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
