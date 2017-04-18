from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$', views.home, name="Home"),
    url("^addGroup/", views.add_group, name="Add Group"),
    url("^deleteGroup/", views.delete_group, name="Delete Group"),
]
