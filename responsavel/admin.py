from django.contrib import admin
from .models import Responsavel

class ResponsavelAdmin(admin.ModelAdmin):
	list_display = ("email", "first_name", "last_name", "cpf")

admin.site.register(Responsavel, ResponsavelAdmin)
