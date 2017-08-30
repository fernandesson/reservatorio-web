from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^3$', views.index3, name='index3'),
    url(r'^download$', views.download, name='download'),
    url(r'^highchart_ex/$', views.highchart_ex, name='highchart_ex'),
]
