from django import forms
from .models import Enquiry

class EnquiryForm(forms.ModelForm):
    class Meta:
        model  = Enquiry
        fields = ['company_name', 'person_name', 'email', 'phone', 'enquiry_details']
        labels = {
            'company_name':    'Company Name',
            'person_name':     'Person Name',
            'email':           'Email Address',
            'phone':           'Phone Number',
            'enquiry_details': 'Enquiry Details',
        }
        widgets = {
            'enquiry_details': forms.Textarea(attrs={'rows': 5, 'placeholder': 'Write your enquiry...'}),
            'company_name':    forms.TextInput(attrs={'placeholder': 'Enter company name'}),
            'person_name':     forms.TextInput(attrs={'placeholder': 'Enter your name'}),
            'email':           forms.EmailInput(attrs={'placeholder': 'Enter email address'}),
            'phone':           forms.TextInput(attrs={'placeholder': 'Enter phone number'}),
        }