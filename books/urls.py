from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from .forms import CommentForm
from .views import *

urlpatterns = [
    path('', views.index, name="index"),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),

]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
