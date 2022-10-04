from django import forms

class EnderecoForm(forms.Form):
    rua= forms.CharField()
    numero = forms.IntegerField()