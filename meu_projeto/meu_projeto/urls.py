from django.contrib import admin
from django.urls import path
from clientes.views import inserir_cliente

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inserir/', inserir_cliente, name='inserir_cliente'),
]
