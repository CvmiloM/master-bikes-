from django.urls import path
from . import views

from django.urls import path
from . import views

from mainapp.views import (
    index, CustomLoginView, CustomLogoutView
)
urlpatterns = [
    path('', views.index, name='index'),
    path('clientes/', views.clientes, name='clientes'),
    path('solicitudes/', views.solicitudes, name='solicitudes'),
    path('solicitud/<int:solicitud_id>/', views.detalle_solicitud, name='detalle_solicitud'),
    path('solicitud/<int:solicitud_id>/confirmar/', views.confirmar_solicitud, name='confirmar_solicitud'),
    path('solicitud/<int:solicitud_id>/rechazar/', views.rechazar_solicitud, name='rechazar_solicitud'),
    path('historial/', views.historial, name='historial'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
]
