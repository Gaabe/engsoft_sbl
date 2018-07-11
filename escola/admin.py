from django.contrib import admin
from .models import Escola

class EscolaAdmin(admin.ModelAdmin):
	list_display = ("nome", "cnpj")

admin.site.register(Escola, EscolaAdmin)
