from django import forms
from .models import Complaint
class Complaintform(forms.ModelForm):
    class Meta:
        model  = Complaint
        fields = ["title","content"]
