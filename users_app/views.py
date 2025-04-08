from django.shortcuts import render, redirect
from .forms import customRegisterForm
from django.contrib import messages

# Create your views here.


def register(request):
    if request.method == "POST":
        register_form = customRegisterForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, 'New Account has Created')
            return redirect('register')
    else:
        register_form = customRegisterForm()
    return render(request, 'register.html', {"register_form": register_form})
