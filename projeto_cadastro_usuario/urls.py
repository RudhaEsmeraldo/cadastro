from django.urls import path
from app_cadastro_usuarios import views

urlpatterns = [
    # rota, view responsável, nome de referência
    # instagram.com -> path()
    # instagram.com/rudhaesmeraldo -> path('rudhaesmeralo')
    path('', views.home, name='home'),
]