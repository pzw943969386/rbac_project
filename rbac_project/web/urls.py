# -- coding: utf-8 --

from django.conf.urls import re_path
from web.views import customer
from web.views import payment
from web.views import account

urlpatterns = [

    re_path(r'^customer/list/$', customer.customer_list,name='customer'),
    re_path(r'^customer/add/$', customer.customer_add,name='customer_add'),
    re_path(r'^customer/edit/(?P<cid>\d+)/$', customer.customer_edit, name='customer_edit'),
    re_path(r'^customer/del/(?P<cid>\d+)/$', customer.customer_del, name='customer_del'),

    re_path(r'^payment/list/$', payment.payment_list, name='payment'),
    re_path(r'^payment/add/$', payment.payment_add, name='payment_add'),
    re_path(r'^payment/edit/(?P<pid>\d+)/$', payment.payment_edit, name='payment_edit'),
    re_path(r'^payment/del/(?P<pid>\d+)/$', payment.payment_del, name='payment_del'),


    re_path(r'^login/$',account.login)
]