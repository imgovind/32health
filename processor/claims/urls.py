from claims import views
from django.urls import re_path

urlpatterns=[
    # re_path(r'^claims$', views.claimsApi),
    # re_path(r'^claims/([0-9]+)$', views.claimsApi)
    re_path(r'^claims$',views.claimsApi),
    re_path(r'^claims/([0-9]+)$',views.claimsApi),
]