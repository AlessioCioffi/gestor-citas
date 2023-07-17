from django.urls import path
from .views import Requests, Request, CreateRequest, UpdateSolicitud, DeleteSolicitud

urlpatterns = [
    path('',Requests.as_view(),name='requests'),
    path('<int:pk>/', Request.as_view(), name='request'),
    path('nueva-solicitud/', CreateRequest.as_view(), name='create_request'),
    path('editar-solicitud-num/<int:pk>/', UpdateSolicitud.as_view(), name='update_request'),
    path('eliminar-solicitud-num/<int:pk>/', DeleteSolicitud.as_view(), name='delete_request')
]