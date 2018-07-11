from django.forms import ModelForm
from .models import Responsavel
from django.core.exceptions import ValidationError

class ResponsavelForm(ModelForm):
	class Meta:
		model = Responsavel
		fields = ['first_name', 'last_name', 'email', 'endereco', 'cpf']

	def clean(self):
		email = self.cleaned_data['email']
		if Responsavel.objects.filter(email=email):
			raise ValidationError(u"Email já cadastrado")
		return cleaned_data
