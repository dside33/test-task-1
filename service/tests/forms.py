from django import forms

class TestForm(forms.Form):
    answer = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 5, 'class': 'form-control text-center'}),
        required=True
    )