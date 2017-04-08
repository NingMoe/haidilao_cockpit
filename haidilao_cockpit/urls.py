from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'haidilao_cockpit.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^haidilao/', include('cockpit.urls')),
    url(r'^upload/', include('im.urls')),
)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

