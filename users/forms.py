from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from .models import UserProfile



class UserForm(UserCreationForm):
	'''
	Formulario para hacer handle del user creation
	'''
	first_name = forms.CharField(max_length=30, required=True,
		widget=forms.TextInput(attrs={'placeholder': 'Escribir nombre'}))
	last_name = forms.CharField(max_length=30, required=True,
		widget=forms.TextInput(attrs={'placeholder': 'Escribir apellido'}))
	username = forms.EmailField(max_length=254, required=True,
		widget=forms.TextInput(attrs={'placeholder': 'Escribir correo electronico'}))
	password1 = forms.CharField(
		widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña','class':'password'}))
	password2 = forms.CharField(
		widget=forms.PasswordInput(attrs={'placeholder': 'Confirmar Contraseña','class':'password'}))

	#reCAPTCHA token
	token = forms.CharField(
		widget=forms.HiddenInput())

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'password1', 'password2', )





class AuthForm(AuthenticationForm):
	'''
	Formulario para hacer handle del user autenthification
	'''
	username = forms.EmailField(max_length=254, required=True,
		widget=forms.TextInput(attrs={'placeholder': 'Correo Electronico'}))
	password = forms.CharField(
		widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña','class':'password'}))

	class Meta:
		model = User
		fields = ('username','password', )




class UserProfileForm(forms.ModelForm):
	'''
	Modelo basico para el perfil que respeta los modelos de django
	
	'''
	address = forms.CharField(max_length=100, required=True, widget = forms.HiddenInput())
	town = forms.CharField(max_length=100, required=True, widget = forms.HiddenInput())
	county = forms.CharField(max_length=100, required=True, widget = forms.HiddenInput())
	post_code = forms.CharField(max_length=8, required=True, widget = forms.HiddenInput())
	country = forms.CharField(max_length=40, required=True, widget = forms.HiddenInput())
	longitude = forms.CharField(max_length=50, required=True, widget = forms.HiddenInput())
	latitude = forms.CharField(max_length=50, required=True, widget = forms.HiddenInput())


	class Meta:
		model = UserProfile
		fields = ('address', 'town', 'county', 'post_code',
		 'country', 'longitude', 'latitude')