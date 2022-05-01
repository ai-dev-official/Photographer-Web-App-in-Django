from django import forms


class ContactUs(forms.Form):
    first_name = forms.CharField(max_length = 25)
    last_name = forms.CharField(max_length = 25)
    email_address = forms.EmailField(max_length = 50)
    phone = forms.CharField(max_length = 25)
    address = forms.CharField(max_length = 25)
    subject = forms.CharField(max_length = 25)
    message = forms.CharField(widget = forms.Textarea, max_length = 1000)