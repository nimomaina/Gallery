from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

from . import views

urlpatterns=[

    url('^$',views.pictures,name='pictures'),
    url(r'^search/', views.search_category, name='search_category'),
    url(r'^location/', views.filter_location, name='filter_location'),

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
