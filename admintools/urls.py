from django.urls import path
from .views import *

app_name = 'admintools'

urlpatterns = [
    path('',admintools,name='admintools'),
    path('usermanagment/',usermanagment,name='usermanagment'),
    path('ordersadmin/',orders_administration,name='orders_admin'),
    path('ordersadmin/confirm-ordr-formed-<ref>',orders_shipping_administration_formed,name='orders_shipping_administration_formed'),
    path('ordersshipadmin/',orders_shipping_administration,name='orders_shipping_admin'),
    path('ordersshipadmin/confirm-passed-to-ship-<ref>',orders_shipping_administration_confirm,name='orders_shipping_admin_confirm'),
    path('manage-parts/',PartsManage.as_view(),name='manage-parts'),
    path('create-part-manual/',CreatePart.as_view(),name='create-part-manual'),
    path('update-part/<id>',UpdatePart.as_view(),name='update-part'),
    path('delete-part/<id>',DeletePart.as_view(),name='delete-part'),
]