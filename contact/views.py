from django.shortcuts import render
from .forms import ContactForm
from django.contrib import messages
from django.core.mail import send_mail
# Create your views here.
def contacts_list(request):
    if request.method =='POST':
        newform=ContactForm(request.POST)
        message=request.POST.get('message')
        username=request.POST.get('username')
        send_mail(
            'Appointment',
            message,
            username,
            ['abhianil96@gmail.com'],

        )
        if newform.is_valid():
            messages.success(request,"Your mail is sent")
        else:
            messages.success(request, "Oops , There is a problemin sending mail")
    else:
        newform=ContactForm()
    return render(request,'home/index.html',{})