from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from pages.models import Message
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from pages.forms import newMessage, logs

class MessageView(ListView):
    model = Message
    template_name = "list.html"
    context_object_name = 'messages'

def createMessage(request):
    if request.method == 'POST':
        form = newMessage(request.POST or None)
        if form.is_valid():
            form.save(commit=True)
        else:
            return render(request, 'create.html', {'form': form})
    else:
        form = newMessage()
    return render(request, 'create.html', {'form': form})

def registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            # User.objects.create_user(username=user.username, password=raw_password)
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def loggs(request):
    form = logs()
    return render(request, "logs.html", {'form': form})

def contact(request):
    return render(request, "contact.html", {})

def about(request):
    return render(request, "about.html", {})
