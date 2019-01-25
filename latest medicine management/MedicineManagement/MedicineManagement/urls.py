from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

from patient import views

urlpatterns = [
    path('', views.homepage, name='home'),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^patient/', include('patient.urls')),
    path('admin/', admin.site.urls),
]
