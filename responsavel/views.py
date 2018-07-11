from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
# from .forms import ResponsavelForm
from .models import Responsavel
import sys, json

def register(request):
	if request.method == 'POST':
		data = request.POST.dict()
		r = Responsavel.objects.create(
			first_name = data['first_name'],
			last_name = data['last_name'],
			username = data['email'],
			email = data['email'],
			endereco = data['endereco'],
			cpf = data['cpf']
		)
		r.set_password(data['password'])
		messages.add_message(request, messages.SUCCESS, 'Cadastro realizado com sucesso')
		return HttpResponseRedirect('/admin/')
	return render(request, 'register.html')

# def register(request):
# 	if request.method == 'POST':
# 		form = ResponsavelForm(request.POST)
# 		if form.is_valid():
# 			form.save()
# 			messages.add_message(request, messages.SUCCESS, 'Cadastro realizado com sucesso')
# 			return HttpResponseRedirect('/admin/')
# 	else:
# 		form = ResponsavelForm()
# 	return render(request, 'register.html', {'form': form})
