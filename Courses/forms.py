from django import forms
from django.forms import ClearableFileInput, Textarea


class NewCourseForm(forms.Form):
    name = forms.CharField(max_length=120)
    overview = forms.CharField(max_length=500,widget=forms.Textarea(attrs={"rows":5, "cols":20}))
    files = forms.FileField(required=False,widget=forms.ClearableFileInput(attrs={'multiple': True}))
