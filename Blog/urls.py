from django.conf.urls import patterns, include, url
from django.contrib import admin
from dashing.utils import router
from django.conf import settings

urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^dashboard/',include(router.urls)),
                       )
