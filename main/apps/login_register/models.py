from django.db import models
from django.core.validators import validate_email
class UserManager(models.Manager):
	def basic_validator(self, postData):
		errors = {}
		if len(postData['Fname']) < 2 or any(i.isdigit() for i in postData['Fname']):
			errors['Fname'] = "Please enter your first name and cannot contain number"
		if len(postData['Lname']) < 2 or any(i.isdigit() for i in postData['Lname']):
			errors['Lname'] = "Please enter your last name and connot contain number"
		if len(postData['password']) <2:
			errors['password'] = "Please enter your password"
		elif len(postData['password']) < 8:
			errors['password'] = "Password must be at least 8 characters"
		if len(postData['con_password']) <1:
			errors['con_password'] = "Please enter your password again"
		elif postData['con_password'] != postData['password']:
			errors['con_password'] = "Your password should match"
		if len(postData['email']) <1:
			print('no email entered')
			errors['email'] = "Please enter your email"
		else:
			try:
				validate_email(postData['email'])
			except:
				errors['email'] = "Email is invalid"

		if User.objects.filter(email = postData['email']):
				print('email existed')
				errors['email'] = "Email already existed in the system"

		return errors
	def login_validator(self, postData):
		errors = {}
		print('login_validator')
		print(postData)
		if len(postData["email"]) <1:
			errors['email'] = "Please enter your email"
		else:
			try:
				validate_email(postData['email'])
			except:
				errors['email'] = "Email is invalid"
				
		if len(postData['password']) < 1:
			errors['password'] = "Please enter your password"
		elif len(postData['password']) < 8:
			errors['password'] = "Password at least 8 characters"
		return errors

class User(models.Model):
	first_name = models.CharField(max_length = 255)
	last_name = models.CharField(max_length = 255)
	email = models.CharField(max_length = 255)
	password = models.CharField(max_length = 255)
	created_at = models.DateTimeField(auto_now_add= True)
	updated_at = models.DateTimeField(auto_now= True)

	objects = UserManager()
