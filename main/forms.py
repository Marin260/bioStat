from tkinter import Label
from django import forms

class UploadFile(forms.Form):
    file = forms.FileField()
    columns = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Eg: 1,2,3'}))
    dateFrom = forms.DateField(label='select starting date', widget=forms.SelectDateWidget())
    dateTo = forms.DateField(label='select ending date', widget=forms.SelectDateWidget())