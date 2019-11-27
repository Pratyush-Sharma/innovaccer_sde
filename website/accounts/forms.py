from django import forms

class NameForm(forms.Form):
    name = forms.CharField(label='name', max_length=100)
    email = forms.EmailField(label='email')
    phone =forms.IntegerField(label='phone',max_value=9999999999,min_value=0)
