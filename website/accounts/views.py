from django.shortcuts import render, HttpResponse,HttpResponseRedirect
from django.core.mail import send_mail
import time
import pytz
from datetime import datetime
from .forms import NameForm
# Create your views here.
def home(request):
    return render(request, 'accounts/home.html')

def myform(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            now =datetime.now(pytz.timezone("Asia/Calcutta"))
            #t = time.asctime(time.localtime(time.time()))

            form_name=form.cleaned_data['name']
            email=form.cleaned_data['email']
            contact=str(form.cleaned_data['phone'])
            t = now.strftime("%d/%m/%Y %H:%M:%S")

            subject="Checked In"
            message="Name- "+form_name+" \n "+"Email- "+email+" \n "
            message=message+"Phone -"+contact+" \n "+"CheckIn Time-"+t
            recipient_list=['sharmatyson007@gmail.com']
            send_mail(subject,message,'sharmatyson007@gmail.com',recipient_list)
            print(form_name)
            return HttpResponseRedirect('/accounts/')

        # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'accounts/login.html', {'form': form})

def outform(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            now =datetime.now(pytz.timezone("Asia/Calcutta"))
            #t = time.asctime(time.localtime(time.time()))

            form_name=form.cleaned_data['name']
            email=form.cleaned_data['email']
            contact=str(form.cleaned_data['phone'])
            t = now.strftime("%d/%m/%Y %H:%M:%S")

            subject="Checked Out"
            message="Name- "+form_name+" \n "+"Email- "+email+" \n "
            message=message+"Phone -"+contact+" \n "+"CheckOut Time-"+t + "\n Host Name - Vishesh Singh"
            message=message + "\n Address visited - Company Office"
            recipient_list=[email]
            send_mail(subject,message,'sharmatyson007@gmail.com',recipient_list)
            print(form_name)
            return HttpResponseRedirect('/accounts/')

        # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'accounts/logout.html', {'form': form})