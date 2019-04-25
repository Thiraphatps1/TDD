from django.conf.urls import include, url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^admin/', admin.site.urls),
]