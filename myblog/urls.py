from django.conf.urls import include, url
from django.contrib import admin

from . import views
import blog.urls


urlpatterns = [
    url(r'^$', views.HomeView.as_view(), name='home'),

    url(r'^', include(blog.urls)),
    url(r'^admin/', admin.site.urls),
]

  
