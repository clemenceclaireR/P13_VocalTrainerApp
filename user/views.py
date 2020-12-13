#! usr/bin/env python3
# -*- Coding: UTF-8 -*-

from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
import uuid
from .forms import UserRegistrationForm, LoginForm


def register(request):
    """
    Register a user account
    """
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)

        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            message = messages.add_message(request, messages.SUCCESS,
                                           'Compte enregistré',
                                           fail_silently=True)

            return render(request,
                          'index.html',
                          locals())
    else:
        user_form = UserRegistrationForm()
    return render(request, 'registration/register.html', locals())


def user_login(request):
    """
    User login management
    """
    if request.method == 'POST':
        login_form = LoginForm(request.POST)

        if login_form.is_valid():
            user = authenticate(request, username=login_form.cleaned_data['username'],
                                password=login_form.cleaned_data['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    message = messages.add_message(request, messages.SUCCESS,
                                                   'Vous êtes désormais authentifié.',
                                                   fail_silently=True)
                    return HttpResponseRedirect('../')
            else:
                message = messages.add_message(request, messages.ERROR,
                                               'Identifiants non reconnus',
                                               fail_silently=True)
                return HttpResponseRedirect('/login')
    else:
        login_form = LoginForm()
    return render(request, 'registration/login.html', locals())