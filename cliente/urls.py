from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from cliente import views

urlpatterns = [
                  path('cadastrar_cli/', views.cadastrar_cli, name="cadastrar_cli"),
                  path('login/', views.login_view, name='login'),
                  path('sair/', views.logout_view, name='logout'),
                  path('menu_cli/', views.menu_cli, name='menu_cli'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)