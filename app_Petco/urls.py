from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio_petco, name='inicio_petco'),
    # URLs para Clientes
    path('clientes/', views.ver_clientes, name='ver_clientes'),
    path('clientes/agregar/', views.agregar_cliente, name='agregar_cliente'),
    path('clientes/actualizar/<int:pk>/', views.actualizar_cliente, name='actualizar_cliente'),
    path('clientes/borrar/<int:pk>/', views.borrar_cliente, name='borrar_cliente'),

    # URLs para Mascotas (NUEVO)
    path('mascotas/', views.ver_mascotas, name='ver_mascotas'),
    path('mascotas/agregar/', views.agregar_mascota, name='agregar_mascota'),
    path('mascotas/actualizar/<int:pk>/', views.actualizar_mascota, name='actualizar_mascota'),
    path('mascotas/borrar/<int:pk>/', views.borrar_mascota, name='borrar_mascota'),
]


