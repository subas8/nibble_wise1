from django import forms


class LoginForm(forms.Form):
	email = forms.EmailField(widget=forms.EmailInput(attrs={
		'placeholder': 'you@example.com',
		'class': 'w-full px-4 py-3 rounded-xl border border-gray-200 focus:ring-2 focus:ring-brand focus:border-brand outline-none'
	}))
	password = forms.CharField(min_length=6, widget=forms.PasswordInput(attrs={
		'placeholder': '••••••••',
		'class': 'w-full px-4 py-3 rounded-xl border border-gray-200 focus:ring-2 focus:ring-brand focus:border-brand outline-none'
	}))


class RegisterForm(forms.Form):
	name = forms.CharField(min_length=2, max_length=50, widget=forms.TextInput(attrs={
		'placeholder': 'Your name',
		'class': 'w-full px-4 py-3 rounded-xl border border-gray-200 focus:ring-2 focus:ring-brand focus:border-brand outline-none'
	}))
	email = forms.EmailField(widget=forms.EmailInput(attrs={
		'placeholder': 'you@example.com',
		'class': 'w-full px-4 py-3 rounded-xl border border-gray-200 focus:ring-2 focus:ring-brand focus:border-brand outline-none'
	}))
	password1 = forms.CharField(min_length=6, widget=forms.PasswordInput(attrs={
		'placeholder': 'Create a password',
		'class': 'w-full px-4 py-3 rounded-xl border border-gray-200 focus:ring-2 focus:ring-brand focus:border-brand outline-none'
	}))
	password2 = forms.CharField(min_length=6, widget=forms.PasswordInput(attrs={
		'placeholder': 'Confirm password',
		'class': 'w-full px-4 py-3 rounded-xl border border-gray-200 focus:ring-2 focus:ring-brand focus:border-brand outline-none'
	}))

	def clean(self):
		cleaned = super().clean()
		p1 = cleaned.get('password1')
		p2 = cleaned.get('password2')
		if p1 and p2 and p1 != p2:
			raise forms.ValidationError('Passwords do not match.')
		return cleaned