from django.conf.urls import url
from . import views

app_name = 'objects'

urlpatterns = [
    url(r'^xml/leads/(?P<size>[0-9]+)/$', views.leads_xml, name='leads_xml'),
    url(r'^json/leads/(?P<size>[0-9]+)/$', views.leads_json, name='leads_json'),
    url(r'^accounts/(?P<dtype>[a-z]+)/(?P<start>[0-9]+)/(?P<end>[0-9]+)/$', views.accounts, name='accounts')
]
