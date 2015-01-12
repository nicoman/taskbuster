from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns
from .views import home, home_files

urlpatterns = patterns('',
    url(r'^(?P<filename>(robots.txt)|(humans.txt))$',
        home_files,
        name='home-files'),
)

urlpatterns += i18n_patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', home, name='home'),
)