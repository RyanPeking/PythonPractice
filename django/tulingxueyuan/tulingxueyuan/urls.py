from django.conf.urls import include, url
from django.contrib import admin
from teacher import views as tv
urlpatterns = [
    # Examples:
    # url(r'^$', 'tulingxueyuan.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^mayiknowyourname/$', tv.revParse, name="askname"),

    url(r'^five_get/', tv.five_get),
    url(r'^five_post/', tv.five_post),
]

