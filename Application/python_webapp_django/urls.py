import app.forms
import app.views
import django.contrib.auth.views
from datetime import datetime
from django.conf.urls import url
from django.views.static import serve
from django.conf import settings
from django.urls import path, include
from django.contrib import admin
from django.conf.urls.static import static
admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', app.views.home, name='home'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
