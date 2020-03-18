from django.urls import include, path, re_path
from .views import *


urlpatterns=[
    re_path(r'^api/leads/(?P<pk>\d+)/$',get_delete_update_lead.as_view(), name='get_delete_update_brand'),
    path('api/leads/',get_post_leads.as_view(), name='get_post_brands'),
]