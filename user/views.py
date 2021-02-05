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
                                           'Compte enregistré. Connectez-vous',
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


@login_required
def user_score_history(request, type_id=None, vowel_type=None):
    """
    User quiz score history
    """
    # get types ids
    consonants = PhonemeType.objects.get(type_name="Consonnes")
    vowels = PhonemeType.objects.get(type_name="Voyelles")
    diphthong = SubPhonemeType.objects.get(id=11)
    simple_vowel = SubPhonemeType.objects.get(id=6)
    # if type_id:
    #     sub_phoneme_type = SubPhonemeType.objects.get(phoneme_type=type_id)

    return render(request, 'user/user_score_history.html', locals())


@login_required
def score_chart(request, type_id=None, vowel_type=None):
    """
    Get user score data, takes optional category
    """
    labels = []
    data = []
    print('type_id '+ str(type_id))

    # by default, if no category is chosen, then takes all category
    if not type_id:
        queryset = Score.objects.values('score', 'date').filter(user_id=request.user).order_by('date')
    else:

        phoneme_type = PhonemeType.objects.get(id=type_id)
        sub_phonemes_types = SubPhonemeType.objects.values_list('id', flat=True).filter(phoneme_type_id=phoneme_type.id)
        if not vowel_type:
            minimal_pairs = MinimalPairCategory.objects.values_list('id', flat=True).filter(sub_phoneme_type_id__in=sub_phonemes_types)
            queryset = Score.objects.values('score', 'date').filter(Q(user_id=request.user) & Q(minimal_pair_category_id_id__in=minimal_pairs))
        else:
            if vowel_type == 11:
                minimal_pairs = MinimalPairCategory.objects.values_list('id', flat=True).filter(
                    sub_phoneme_type_id=vowel_type)

            else:
                vowel_type = PhonemeType.objects.get(type_name="Voyelles")
                simple_vowels = SubPhonemeType.objects.values_list('id', flat=True).filter(phoneme_type_id=vowel_type.id).excludes(id=11)
                minimal_pairs = MinimalPairCategory.objects.values_list('id', flat=True).filter(
                    sub_phoneme_type_id=simple_vowels)
            queryset = Score.objects.values('score', 'date').filter(
                    Q(user_id=request.user) & Q(minimal_pair_category_id__in=minimal_pairs)).order_by('date')

    for entry in queryset:
        labels.append(entry['date'])
        data.append(entry['score'])

    # reformat datetime format to DD-MM-YY string
    labels[:] = [date.strftime('%d-%b-%Y') for date in labels]

    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })
