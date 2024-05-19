from django.shortcuts import render, redirect
from . import models
from django.views import View
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin


class Register(View):
    def get(self, request):
        return render(request, 'registration.html')

    def post(self, request):
        username = request.POST['username']
        first_name = request.POST['first_name']
        age = request.POST['age']
        bio = request.POST['bio']
        password = request.POST['password']

        account = models.Accounts.objects.create_user(
            username=username,
            first_name=first_name,
            age=age,
            bio=bio,

        )
        account.set_password(password)
        account.save()

        return redirect('Login')


class Login(View):
    def get(self, request):
        login_form = AuthenticationForm()
        context = {
            'login_form': login_form
        }
        return render(request, 'login.html', context=context)

    def post(self, request):
        login_form = AuthenticationForm(data=request.POST)
        if login_form.is_valid():
            account = login_form.get_user()
            login(request, account)
            return redirect('dashboard')

        else:
            context = {
                'form': login_form
            }
            return render(request, 'login.html', context=context)


class Logout(View, LoginRequiredMixin):
    def get(self, request):
        logout(request)
        return redirect('dashboard')

# profile
