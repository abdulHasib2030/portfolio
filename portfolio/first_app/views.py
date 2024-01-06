from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from first_app.forms import contactForm
from django.core.mail import send_mail
from django.contrib import messages
# Create your views here.
def home(request):
  return render(request, 'base.html')

def contactView(request):
  if request.method == 'POST':
    form = contactForm(request.POST)
    if form.is_valid():
      subject = form.cleaned_data["subject"]
      message = form.cleaned_data["message"]
      customer_sender = form.cleaned_data["email"]
      cc_myself = form.cleaned_data["name"]
      mess = f'''
Name: {cc_myself},
Email: {customer_sender},
Message: {message}'''
              
      sender = "creative3218@gmail.com"       
      recipients = ["abdulhasib2030@gmail.com",]
    
      customer_message = 'Thanks you for your interest. I will contact you soon.🙂'
      customer_sub = 'Your Contact with Abdul Hasib'
      send_mail(subject, mess, sender, recipients)
      lst = []
      lst.append(customer_sender)
      lst.append('abdulhasib2030@gmail.com')
      re = "abdulhasib2030@gmail.com"

      send_mail(customer_sub, customer_message, re, lst)
      
      messages.success(request, 'Thank you for your interest. I will contact you soon')

      return redirect('home')
      # return render(request, 'base.html', {'form': contactForm(request.GET)})
    else:
        messages.error(request, 'Invalid form submission.')
        messages.error(request, form.errors)
          
      # return HttpResponseRedirect(request.path_info)
    
  return render(request, 'base.html')

