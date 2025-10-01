
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('principal.urls')),
    path('', include('produto.urls')),
    path('', include('categoria.urls')),
    path('', include('cliente.urls')),
    path('', include('carrinho.urls'))
]
