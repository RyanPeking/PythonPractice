from django.conf.urls import include, url
from django.contrib import admin

from teacher_app import views as v

urlpatterns = [
    # Examples:
    # url(r'^$', 'tulingxueyuan_views.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^teacher/', v.teacher),

    url(r'^render2_test/', v.render2_test),

    url(r'^render3_test/', v.render3_test),

    url(r'^render4_test/', v.render4_test),

    url(r'^get404/', v.get404)
]
