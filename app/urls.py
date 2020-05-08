from django.urls import path, include
from django.contrib import admin
from django.conf.urls import url
from django.urls import include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.sitemaps.views import sitemap
from Modulka.sitemaps import PostSitemap

sitemaps = {'posts': PostSitemap,}

urlpatterns = [
    path('',include('Modulka.urls', namespace='Modulka')),
    path('admin/', admin.site.urls),
    path('Modulka/', include('Modulka.urls', namespace='Modulka')),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    path('api/', include('Modulka.urls', namespace='rest_framework')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},name='django.contrib.sitemaps.views.sitemap')
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
  
