from django.contrib.auth import views as auth_views
from django.conf.urls import include, url
from django.contrib import admin
from userrating.views import index

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^userrating/', include('userrating.urls', namespace="userrating")),
    url('^login/', auth_views.login, {'template_name': 'userrating/login.html'},
            name="login"),
    url('^logout/', auth_views.logout, {'next_page': '/login/'}, name="login"),

    url(r'^admin/', include(admin.site.urls)),
]
