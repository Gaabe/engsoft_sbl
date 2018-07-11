from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import ResponsavelForm
from django.contrib import messages

def register(request):
	if request.method == 'POST':
		form = ResponsavelForm(request.POST)
		if form.is_valid():
			form.save()
			messages.add_message(request, messages.SUCCESS, 'Cadastro realizado com sucesso')
			return HttpResponseRedirect('/admin/')
	else:
		form = ResponsavelForm()
	return render(request, 'register.html', {'form': form})
