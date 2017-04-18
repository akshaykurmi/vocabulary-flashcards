from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$', views.groups, name="Home"),
    url('^groups/$', views.groups, name="Groups"),
    url("^addGroup/", views.add_group, name="Add Group"),
    url("^deleteGroup/", views.delete_group, name="Delete Group"),
    url("^editGroup/", views.edit_group, name="Edit Group"),
]
