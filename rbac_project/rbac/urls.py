from django.conf.urls import re_path
from rbac import views

urlpatterns = [
    # /app01/role/list/    # rbac:role_list
    re_path(r'^role/list/$', views.role_list, name='role_list'),
    re_path(r'^role/add/$', views.role, name='role_add'),
    re_path(r'^role/edit/(\d+)$', views.role, name='role_edit'),
    re_path(r'^role/del/(\d+)$', views.del_role, name='role_del'),
    
    re_path(r'^menu/list/$', views.menu_list, name='menu_list'),
    
    re_path(r'^menu/add/$', views.menu, name='menu_add'),
    re_path(r'^menu/edit/(\d+)$', views.menu, name='menu_edit'),
    re_path(r'^permission/add/$', views.permission, name='permission_add'),
    re_path(r'^permission/edit/(\d+)$', views.permission, name='permission_edit'),
    re_path(r'^permission/del/(\d+)$', views.del_permission, name='permission_del'),
]
