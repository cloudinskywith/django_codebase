from django.conf.urls import patterns, include, url
from django.contrib import admin
from dashing.utils import router
from django.conf import settings

urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^dashboard/',include(router.urls)),
                       )
if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/',include(debug_toolbar.urls)),
    ] + urlpatterns


