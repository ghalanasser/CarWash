from django import forms
from .models import Application_by_user

class Application_form(forms.ModelForm):
    class Meta:
        model = Application_by_user
        fields = ('applicantId', 'userName', 'userEmail',
                  'carModel', 'plan', 'appDate')
        widgets = {
            'applicantId': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'userName': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'userEmail': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'carModel': forms.TextInput(
                attrs={
                    'class': 'form-group'
                }
            ),
            'plan': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'appDate': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            )
        }
