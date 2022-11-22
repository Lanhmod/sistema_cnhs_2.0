from atexit import register
from django.contrib import admin
from core_cnhs_2.models import Candidatos
class CandidatosAdmin(admin.ModelAdmin):
    list_display = ( 'nome','cpf', 'telefone', 'data_criacao')
    search_fields = ('cpf','nome',)


    
admin.site.register(Candidatos, CandidatosAdmin)
