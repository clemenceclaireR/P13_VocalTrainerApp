from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Sum, Q
from django.http import JsonResponse
from django.db.models import F, Func, Value, CharField
import datetime
import uuid
from quiz.models import Score
from minimal_pair.models import MinimalPairCategory
from api_board.models import SubPhonemeType, PhonemeType
from .forms import UserRegistrationForm, LoginForm


def register(request):
    """
    Register a user account
    """
    user_form = UserRegistrationForm()
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)

        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            message = messages.add_message(request, messages.SUCCESS,
                                           'Compte enregistré',
                                           fail_silently=True)

            return redirect(reverse('api_board:index'))

    return render(request, 'registration/register.html', locals())


def user_login(request):
    """
    User login management
    """
    login_form = LoginForm()
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
    return render(request, 'registration/login.html', locals())


def user_score_history(request):
    """
    User quiz score history
    """
    # get types ids
    consonant_type = PhonemeType.objects.get(id=1)
    vowel_type = PhonemeType.objects.get(id=2)

    return render(request, 'user/user_score_history.html', locals())


@login_required
def score_chart(request):
    """
    Get user score data, takes optional category
    """
    labels = []
    data = []

    # by default, if no category is chosen, then takes all category


    queryset = Score.objects.values('score', 'date').filter(user_id=request.user).order_by('date')

        # parent_type = PhonemeType.objects.get(id=cat)
        # sub_type = MinimalPairCategory.objects.values_list('id', flat=True).filter(sub_phoneme_type_id__in=parent_type)
        # queryset = Score.objects.values('score', 'date').filter(
        # (Q(user_id=request.user) & Q(minimal_pair_category_id__in=sub_type))).order_by('date')

    for entry in queryset:
        labels.append(entry['date'])
        data.append(entry['score'])

    # reformat datetime format to DD-MM-YY string
    labels[:] = [date.strftime('%d-%b-%Y') for date in labels]

    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })
