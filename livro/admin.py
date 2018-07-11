from django.contrib import admin
from .models import Livro, Indicacao

class LivroAdmin(admin.ModelAdmin):
	list_display = ("isbn", "titulo", "autor", "editora", "edicao", "ano_de_publicacao")

class IndicacaoAdmin(admin.ModelAdmin):
	list_display = ("livro", "escola", "ano", "serie", "tipo", "nivel", "preco_sugerido")

admin.site.register(Livro, LivroAdmin)
admin.site.register(Indicacao, IndicacaoAdmin)