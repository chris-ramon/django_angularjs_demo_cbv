from django.conf.urls import patterns, include, url
from demo_app.views import PostList, PostDetail

# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^posts$', PostList.as_view(), name='post_list'),
    url(r'^posts/(?P<pk>[^/]+)$', PostDetail.as_view(), name='post_detail'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^admin/', include(admin.site.urls)),
)
