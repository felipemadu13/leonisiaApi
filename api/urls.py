
from django.contrib import admin
from django.urls import path, include
from api import views

from .views import user_login, user_logout, user_register

urlpatterns = [
    path('register/', user_register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),

    # Dashboard
    path('dashboard/', views.dashboard_view, name='dashboard'),

    # Serviços
    path('servicos/', views.get_servicos, name='get_all_servicos'),
    path('servicos/<int:id>/', views.get_servicos_by_id, name='get_servicos_by_id'),

    # Serviços Realizados
    path('servicosrealizados/', views.get_servicos_realizados, name='get_all_servicos_realizados'),
    path('servicosrealizados/<int:id>/', views.get_servicos_realizados_by_id, name='get_servicos_by_id'),
    path('servicosrealizados/servicos-realizados-transacoes/', views.get_servicos_e_transacoes),
    
    # Transações
    path('transacoes/', views.get_transacoes, name='transacoes'),
    path('transacoes/<int:id>/', views.get_transacoes_by_id, name='transacoes_id'),

]
