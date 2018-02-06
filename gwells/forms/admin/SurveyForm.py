from django import forms

class SurveyForm(forms.form):
    survey_name = forms.CharField(label='Survey Name', max_length=64)
