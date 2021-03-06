from django.db import models
from escola.models import Escola

SERIE_CHOICES = ((1, "1ª"), (2, "2ª"), (3, "3ª"), (4, "4ª"), (5, "5ª"), (6, "6ª"), (7, "7ª"), (8, "8ª"))
NIVEL_CHOICES = ((1, "Fundamental"), (2, "Médio"))
TIPO_CHOICES = ((1, "Didático"), (2, "Paradidático"))

class Livro(models.Model):

	class Meta:
		verbose_name = 'Livro'
		verbose_name_plural = 'Livros'
		app_label = "livro"

	isbn = models.CharField(max_length=200)
	titulo = models.CharField(max_length=200, verbose_name="Título")
	autor = models.CharField(max_length=200)
	editora = models.CharField(max_length=200)
	edicao = models.CharField(max_length=200, verbose_name="Edição")
	ano_de_publicacao = models.CharField(max_length=200, verbose_name="Ano de publicação")

	def __str__(self):
		return "{isbn} - {titulo}".format(isbn=self.isbn, titulo=self.titulo)

class Indicacao(models.Model):

	class Meta:
		verbose_name = 'Indicação'
		verbose_name_plural = 'Indicações'
		app_label = "livro"

	escola = models.ForeignKey(Escola, on_delete=models.CASCADE)
	ano = models.CharField(max_length=4)
	serie = models.IntegerField(choices=SERIE_CHOICES, verbose_name="Série")
	nivel = models.IntegerField(choices=NIVEL_CHOICES, verbose_name="Nível")
	tipo = models.IntegerField(choices=TIPO_CHOICES)
	preco_sugerido = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Preço sugerido")
	livro = models.ForeignKey(Livro, on_delete=models.CASCADE)

	def __str__(self):
		return self.livro