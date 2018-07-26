from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^sales/$', views.sales_list, name='sales'),
    url(r'^purchases/$', views.purchases_list, name='purchases'),
]