from django import forms
from .models import *

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = "__all__"

    def save(self, commit=True):
        patient = super(PatientForm, self).save(commit=False)
        if commit:
            patient.save()
        return patient