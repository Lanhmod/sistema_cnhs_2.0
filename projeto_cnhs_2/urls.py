"""projeto_cnhs_2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from core_cnhs_2 import views 

app_name = 'Detran - SCC'

#após as alterações das model devo alterar também as views e depois reconfigurar as urls
urlpatterns = [
    path('admin/', admin.site.urls), #redirecionamento para a area de administrador 
    path('login/', views.login_usuarios, name='login'), #area de login 
    path('login/submit', views.submit_login), #autenticação de senha e nome 
    path('logout/', views.logout_usuarios, name='logout'), #saída da conta
    path('lista_candidatos/', views.lista_candidatos, name='lista_candidatos'),#lista de visualização de candidatos
    path('lista_candidatos_update/', views.lista_candidatos_update, name='lista_candidatos_update'), #lista de candidados para consulta e alteração de dados
    path('lista_candidatos_correcao/', views.lista_candidatos_correcao, name='lista_candidatos_correcao'),
    path('inscricao_candidatos/', views.form_inscrição, name='form_inscricao'), #formulario de inscrição do candidato
    path('jm/<str:id>/', views.form_atualizacao_jm, name='form_atualizacao_jm'),
    path('crt/<str:id>/', views.form_atualizacao_crt, name='form_atualizacao_crt' ), 
    path('cedv/<str:id>/', views.form_atualizacao_cedv, name='form_atualizacao_cedv'),
    path('cnh/<str:id>/', views.form_atualizacao_cnh, name='form_atualizacao_cnh'),
    path('correcao_jm/<str:id>/', views.form_correcao_jm, name='form_correcao_jm'),
    path('correcao_crt/<str:id>/', views.form_correcao_crt, name='form_correcao_crt' ), 
    path('correcao_cedv/<str:id>/', views.form_correcao_cedv, name='form_correcao_cedv'),
    path('correcao_cnh/<str:id>/', views.form_correcao_cnh, name='form_correcao_cnh'),
    path('', views.home, name='home'),
    path('instrucoes/', views.instrucoes, name='instrucoes'),
]
