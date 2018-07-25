from django.contrib import admin
from .models import Livro, Indicacao, Exemplar

def comprar_exemplar(modeladmin, request, queryset):
    single = queryset.first()._meta.verbose_name
    mult = queryset.first()._meta.verbose_name_plural
    count = 0
    for exemplar in queryset:
        exemplar.vendido = False
        exemplar.em_venda = False
    msg_name = mult if count > 1 else single
    messages.success(request, "Comprado {} {} selecionado{} com sucesso.".format(count, msg_name,
                        's' if count > 1 else ''))
comprar_exemplar.short_description = "Comprar os exemplares selecionados"

def criar_exemplar(modeladmin, request, queryset):
    single = queryset.first()._meta.verbose_name
    for livro in queryset:
        Exemplar.objects.create(livro = livro)
        break # somente o primeiro => resolver para retirar multiselect
    messages.success(request, "Criado 1 exemplar com sucesso")
criar_exemplar.short_description = "Criar um exemplar do modelo selecionado"

class LivroAdmin(admin.ModelAdmin):
    list_display = ("isbn", "titulo", "autor", "editora", "edicao", "ano_de_publicacao")
    actions = [criar_exemplar]

class IndicacaoAdmin(admin.ModelAdmin):
    list_display = ("livro", "escola", "ano", "serie", "tipo", "nivel", "preco_sugerido")

def deactive_selected(modeladmin, request, queryset):
    single = queryset.first()._meta.verbose_name
    mult = queryset.first()._meta.verbose_name_plural
    count = 0
    for user in queryset:
        user.is_active = False
        user.save()
        count = count + 1
    msg_name = mult if count > 1 else single
    messages.success(request, "Desativado {} {} selecionado{} com sucesso.".format(count, msg_name,
                     's' if count > 1 else ''))
deactive_selected.short_description = "Desativar os Usuários selecionados"

class ExemplarAdmin(admin.ModelAdmin):
    list_display = ['livro_titulo', 'livro_autor', 'livro_editora', 'estado', 'em_venda', 'vendido']
    list_filter = ('estado', 'em_venda', 'vendido',)
    search_fields = ('livro__titulo', 'livro__autor', 'livro__editora')
    fields = ("__all__",)
    actions = [comprar_exemplar]

admin.site.register(Livro, LivroAdmin)
admin.site.register(Indicacao, IndicacaoAdmin)
admin.site.register(Exemplar, ExemplarAdmin)