from django import forms

class ContactForm(forms.Form):
    name=forms.CharField(max_length=50)
    username=forms.EmailField()
    company_name=forms.CharField(max_length=50)
    message=forms.Textarea()
    contact_number=forms.CharField(max_length=20)

