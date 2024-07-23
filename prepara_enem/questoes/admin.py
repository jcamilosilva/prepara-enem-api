from django.contrib import admin
from .models import Questao, Ano, Materia, Assunto

class QuestaoAdmin(admin.ModelAdmin):
    list_display = ('numero', 'ano', 'materia', 'get_assuntos', 'enunciado')
    filter_horizontal = ('assuntos',)  # Adiciona um widget de seleção múltipla horizontal

    def get_assuntos(self, obj):
        return ", ".join([assunto.nome for assunto in obj.assuntos.all()])
    get_assuntos.short_description = 'Assuntos'

admin.site.register(Questao, QuestaoAdmin)
admin.site.register(Ano)
admin.site.register(Materia)
admin.site.register(Assunto)
