from django.conf.urls import patterns, url, include
from blog.views import index

urlpatterns = patterns('',
	url(r'index/(?P<page_num>\d+)$', 'blog.views.index'),
)