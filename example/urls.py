from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

from example import views

urlpatterns = [

     # re_path(r'^example_lista/$', views.ExampleList.as_view() ),
     # re_path(r'^example_detail/(?P<id>\d+)$', views.ExampleDetail.as_view() ),

     
     #urls extra
     re_path(r'^lista_productos/$', views.ProductsList.as_view() ),
     #re_path(r'^listaiproductos/$', views.InventoriesFList.as_view() ),
     re_path(r'^lista_productosall/$', views.ProductListAll.as_view() ),
     re_path(r'^detalle_producto/(?P<id>\d+)$', views.ProductDetail.as_view() ),
     re_path(r'^inventarioview/$', views.InventorytListAll.as_view() ),
     #re_path(r'^grupos_profesores/(?P<id>\d+)$', views.GruposPPDetail.as_view() ),
     #re_path(r'^grupos_alumno/(?P<id>\d+)$', views.GruposPDetail.as_view() ),  InventoriesPviewDetail
     

     re_path(r'^users_lista/$', views.UsersList.as_view() ),
     re_path(r'^users_detail/(?P<id>\d+)$', views.UserDetail.as_view() ),
     
     re_path(r'^inventario_lista/$', views.InventoriesList.as_view() ),
     re_path(r'^inventario_detail/(?P<id>\d+)$', views.InventoriesDetail.as_view() ),
     re_path(r'^inventariod_view/(?P<id>\d+)$', views.InventoriesviewDetail.as_view() ),
     #re_path(r'^inventariodPview/(?P<id>\d+)$', views.InventoriesPviewDetail.as_view() ),

     re_path(r'^transaccion_lista/$', views.TransactionsList.as_view() ),
     re_path(r'^transaccionview/$', views.TransactiontListAll.as_view() ),
     re_path(r'^transaccion_detail/(?P<id>\d+)$', views.TransactionDetail.as_view() ),
     re_path(r'^transaccionviewdetail/(?P<id>\d+)$', views.TransactionviewDetail.as_view() ),

     re_path(r'^sales_lista/$', views.SalesList.as_view() ),
     re_path(r'^sales_detail/(?P<id>\d+)$', views.SaleDetail.as_view() ),
     re_path(r'^canselar_venta/$', views.CancelSale.as_view() ),
     re_path(r'^salesviewlista/$', views.SalesviewList.as_view() ),
]