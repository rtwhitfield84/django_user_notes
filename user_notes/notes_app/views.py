from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth import logout, login, authenticate
from django.http import HttpResponse, HttpResponseRedirect
from . models import OneNote





class IndexView(TemplateView):
	template_name = 'notes_app/login.html'

class LoginSuccess(LoginRequiredMixin, TemplateView):
	template_name = 'notes_app/home.html'

class Register(TemplateView):
	template_name = 'notes_app/register.html'

class NewNote(TemplateView):
	template_name = 'notes_app/new_note.html'

def register_user(request):
	data = request.POST
	User.objects.create_user(
		username=data['username'],
		email=data['email'],
		first_name=data['first_name'],
		last_name=data['last_name'],
		password=data['password']
	)

	return login_user(request)

def login_user(request):
	data = request.POST
	username = data['username']
	password = data['password']
	user = authenticate(
		username=username,
		password=password
	)

	if user is not None:
		login(request=request, user=user)
	else:
		HttpResponseRedirect(redirect_to='/')
	return HttpResponseRedirect(redirect_to='/my_notes')

def logout_user(request):
	logout(request)
	return HttpResponseRedirect(redirect_to='/')

def add_note(request):
	data = request.POST
	OneNote.objects.create(
		title=data['title'],
		note=data['note'],
		author=data['user']
	)

	return HttpResponseRedirect(redirect_to='/my_notes')












