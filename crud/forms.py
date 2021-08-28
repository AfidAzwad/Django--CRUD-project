from  django import forms
from django.db.models import fields
from crud import models

class Userform(forms.ModelForm):
    class Meta:
        model = models.Students
        fields = "__all__"