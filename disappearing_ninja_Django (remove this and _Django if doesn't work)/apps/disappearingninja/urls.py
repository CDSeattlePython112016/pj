from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^result$', views.result),
    url(r'^ninjas/(?P<color>\w+)*$', views.processninjas)
]
