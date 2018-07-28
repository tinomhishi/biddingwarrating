from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^sales/$', views.sales_list, name='sales'),
    url(r'^purchases/$', views.purchases_list, name='purchases'),
    url(r'^purchases/(?P<pk>[0-9]+)/$', views.purchase_detail, name='purchase_detail'),
    url(r'^sales/(?P<pk>[0-9]+)/$', views.sale_detail, name='sale_detail'),
   
]