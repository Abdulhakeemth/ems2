from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from account.models import Account


# class TeacherForm(UserCreationForm):
# 	password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control pwstrength','data-indicator':'pwindicator'},))
# 	password2 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control pwstrength','data-indicator':'pwindicator'},))
# 	class Meta:
# 		model = Account
# 		fields = ('email', 'username','address','phone','full_name')
# 		widgets= {
# 			'username' : forms.TextInput(attrs={'class': 'required form-control',}),
# 			'full_name' : forms.TextInput(attrs={'class': 'required form-control',}),
# 			'email' : forms.TextInput(attrs={'class': 'required form-control',}),
# 			'address' : forms.Textarea(attrs={'class': 'required form-control',}),
# 			'phone' : forms.NumberInput(attrs={'class': 'required form-control','type' : 'tel','maxlength' : '10'}),
			
# 		}
		
# class UpdateTeacherForm(forms.ModelForm):
# 	class Meta:
# 		model = Account
# 		fields = ('email', 'username','address','phone','full_name')
# 		widgets= {
# 			'username' : forms.TextInput(attrs={'class': 'required form-control',}),
# 			'full_name' : forms.TextInput(attrs={'class': 'required form-control',}),
# 			'email' : forms.TextInput(attrs={'class': 'required form-control',}),
# 			'address' : forms.Textarea(attrs={'class': 'required form-control',}),
# 			'phone' : forms.NumberInput(attrs={'class': 'required form-control','type' : 'tel','maxlength' : '10'}),
			
# 		}

class RegistrationForm(UserCreationForm):
	email = forms.EmailField(max_length=254, widget=forms.EmailInput(attrs={'class':'form-control'},))
	password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control pwstrength','data-indicator':'pwindicator'},))
	password2 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'},))

	class Meta:
		model = Account
		fields = ('email','address','phone','username')
		widgets= {
			'username' : forms.TextInput(attrs={'class': 'required form-control',}),
			'address' : forms.Textarea(attrs={'class': 'required form-control',}),
			'phone' : forms.NumberInput(attrs={'class': 'required form-control','type' : 'tel','maxlength' : '10'}),
			'district':forms.Select(attrs={'class': 'required form-control'}),
		}

	def clean_email(self):
		email = self.cleaned_data['email'].lower()
		try:
			account = Account.objects.exclude(pk=self.instance.pk).get(email=email)
		except Account.DoesNotExist:
			return email
		raise forms.ValidationError('Email "%s" is already in use.' % account)

	# def clean_username(self):
	# 	username = self.cleaned_data['username']
	# 	try:
	# 		account = Account.objects.exclude(pk=self.instance.pk).get(username=username)
	# 	except Account.DoesNotExist:
	# 		return username
	# 	raise forms.ValidationError('Username "%s" is already in use.' % username)


class AccountAuthenticationForm(forms.ModelForm):

	password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'required form-control',}))
	phone = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control','max_length':'10'},))
	class Meta:
		model = Account
		fields = ('phone', 'password')

	def clean(self):
		if self.is_valid():
			phone = self.cleaned_data['phone']
			password = self.cleaned_data['password']
			if not authenticate(phone=phone, password=password):
				raise forms.ValidationError("Invalid login")


class AccountUpdateForm(forms.ModelForm):

	class Meta:
		model = Account
		fields = ('email', 'phone', )

	def clean_email(self):
		email = self.cleaned_data['email'].lower()
		try:
			account = Account.objects.exclude(pk=self.instance.pk).get(email=email)
		except Account.DoesNotExist:
			return email
		raise forms.ValidationError('Email "%s" is already in use.' % account)

	# def clean_username(self):
	# 	username = self.cleaned_data['username']
	# 	try:
	# 		account = Account.objects.exclude(pk=self.instance.pk).get(username=username)
	# 	except Account.DoesNotExist:
	# 		return username
	# 	raise forms.ValidationError('Username "%s" is already in use.' % username)
















