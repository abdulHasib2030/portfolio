from django import forms

class contactForm(forms.Form):
  name = forms.CharField(label="name", max_length=100)
  email = forms.EmailField(label="email", max_length=100)
  subject = forms.CharField(label="subject", max_length=200)
  message = forms.CharField(label="message", max_length=1000)
    
