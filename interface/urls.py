from django.conf.urls import patterns, url
from views import game_page

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r"$", game_page),
)
