from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^info/$', views.resource, name='info'),
    url(r'^delete/images/$', views.delete_container_or_image, {'method':'delete'}, name='image'),
    url(r'^delete/containers/$', views.delete_container_or_image, {'method': 'delete'}, name='container'),
    url(r'^new/container/$', views.new_container, name='new'),
    url(r'^containers/(?P<name>[\w|-]+)/stats/$', views.container_resource_stats),
    url(r'^get/resource_usage/(?P<name>[\w|-]+)/$', views.add_thread_for_get_resource_usage),
]
