from django import forms
from django.forms import modelformset_factory

from new_app.models import Candidate, Education

class CandidateForm(forms.ModelForm):
    class Meta:
        model = Candidate
        fields = ('__all__')

class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ('__all__')

EducationFormSet = modelformset_factory(
    Education, form=EducationForm, extra=1, can_delete=True
)