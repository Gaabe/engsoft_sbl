from django.db import models

class Escola(models.Model):

	class Meta:
		verbose_name = 'Escola'
		verbose_name_plural = 'Escolas'
		app_label = "escola"

	nome = models.CharField(max_length=200)
	cnpj = models.CharField(max_length=20)
	endereco = models.CharField(max_length=200)

	def __str__(self):
		return self.nome
