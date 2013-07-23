from django import forms

class Address(forms.Form):
	address = forms.CharField()
	city = forms.CharField()
	state = forms.CharField(max_length=2)