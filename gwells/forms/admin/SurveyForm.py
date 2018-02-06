from django import forms

class SurveyForm(forms.Form):
    survey_name = forms.CharField(label='Survey Name', max_length=64)
