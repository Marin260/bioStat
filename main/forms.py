from faulthandler import disable
from django import forms


H_SAMPLE =(
    ("1H", "1H"),
    ("4H", "4H"),
    ("12H", "12H"),
    ("24H", "24H")
)
MATH_FS =(
    ("1", "MEAN"),
    ("2", "SUM")
)
class UploadFile(forms.Form):
    file = forms.FileField()
    columns = forms.CharField(label='Selected Columns', required=False)
    dateFrom = forms.DateTimeField(label='select starting date')
    dateTo = forms.DateTimeField(label='select ending date')
    sampling = forms.ChoiceField(choices=H_SAMPLE)
    selected_function = forms.ChoiceField(choices=MATH_FS)