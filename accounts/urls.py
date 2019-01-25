from django.conf.urls import url
from accounts.forms import CustomAuthForm
from django.contrib.auth import views as auth_views

app_name = 'accounts'

urlpatterns = [

    url(r'^login/$', auth_views.login, name='login', kwargs={"authentication_form": CustomAuthForm}),
    url(r'^logout/$', auth_views.logout, name='logout'),
]
