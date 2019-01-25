from django.conf.urls import url

from patient import views

app_name = 'accounts'

urlpatterns = [

    url(r'^add_patient', views.add_patinet_view, name='add'),
    url(r'^register', views.register_user, name='register'),
    url(r'^(?P<pk>[0-9]+)', views.patient_detail, name='delete_item'),
    url(r'^all_patients', views.all_patients, name='all_patients'),
    url(r'^all_meds', views.all_meds, name='all_meds'),

    ]