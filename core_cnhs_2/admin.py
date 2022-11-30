from django.contrib import admin
from core_cnhs_2.models import Candidatos
class CandidatosAdmin(admin.ModelAdmin):
    list_display = ( 'nome','cpf', 'telefone', 'data_criacao')
    search_fields = ('cpf','nome',)

    class Meta:
        ordering = ('data_criacao',)

    
admin.site.register(Candidatos, CandidatosAdmin)
