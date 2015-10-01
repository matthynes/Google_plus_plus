from django.conf.urls import include, url
from django.contrib import admin

from posts import views as post_views

admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', post_views.index, name='homepage'),
]
