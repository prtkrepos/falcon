from django.conf.urls import patterns, url
from views import problem_page

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r"^/(?P<id>[0-9]+)/$", problem_page),
)
