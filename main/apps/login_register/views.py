from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import *
import bcrypt

def index(request):
	return render(request, 'index.html'	)

def register(request):
	errors = User.objects.basic_validator(request.POST)
	if len(errors):
		for key, value in errors.items():
			messages.error(request, value)
		return redirect('/')
	else:
		hashpw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
		User.objects.create(
			first_name = request.POST['Fname'],
			last_name = request.POST['Lname'],
			email = request.POST['email'],
			password = hashpw
			)
		return redirect('/success')

def success(request):
	return render(request, 'success.html')

def login(request):
	print("-------------- - - - ")
	print(request.POST)
	errors = User.objects.login_validator(request.POST)
	if len(errors):
		print('error')
		for key, value in errors.items():
			messages.error(request, value)
		return redirect('/')
	else:
		print('get email')
		user = User.objects.filter(email = request.POST['email'])
		if user :
			if bcrypt.checkpw(request.POST['password'].encode(), user[0].password.encode()) == False:
				print("invalid")
				messages.error(request, "invalid password")
				return redirect('/')
			else:
				print('pass')
				return redirect('/login_success')
		else:
			return redirect('/')


def login_success(request):

	return render(request, 'login.html')