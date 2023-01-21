"""tastyblog URL Configuration"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', include('books.urls'), name='books.urls'),
    path('summernote/', include('django_summernote.urls')),
]
