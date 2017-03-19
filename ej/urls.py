from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views
from . import views
from .forms import PostForm

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^post/(?P<pk>\d+)/remove/$', views.post_remove, name='post_remove'),
    url(r'^accounts/login/$', views.login, name='login'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('ej.urls')),
]
