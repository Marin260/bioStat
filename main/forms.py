from faulthandler import disable
from django import forms


H_SAMPLE =(
    ("1H", "1H"),
    ("4H", "4H"),
    ("12H", "12H"),
    ("24H", "24H")
)
MATH_FS =(
    ("MEAN", "MEAN"),
    ("SUM", "SUM")
)
class UploadFile(forms.Form):
    file = forms.FileField()
    columns = forms.CharField(label='Delete Columns', required=False, widget=forms.TextInput(attrs={'placeholder': 'Eg.: A, B, 10, 12, 34, 16'}))
    dateFrom = forms.DateTimeField(label='Select starting date', widget=forms.TextInput(attrs={'placeholder': 'Eg.: 2019-12-21T08:00'}))
    dateTo = forms.DateTimeField(label='Select ending date', widget=forms.TextInput(attrs={'placeholder': 'Eg.: 2019-12-29T08:00'}))
    sampling = forms.ChoiceField(choices=H_SAMPLE)
    selected_function = forms.ChoiceField(choices=MATH_FS)