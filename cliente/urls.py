from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from cliente.views import cadastrar_cli, login_view, logout_view, menu_cli, buscar_endereco
urlpatterns = [
                  path('cadastrar_cli/', cadastrar_cli, name="cadastrar_cli"),
                  path('login/', login_view, name='login'),
                  path('sair/', logout_view, name='logout'),
                  path('menu_cli/', menu_cli, name='menu_cli'),
                  path('buscar_endereco/', buscar_endereco, name='buscar_endereco'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)