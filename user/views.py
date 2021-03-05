from django.shortcuts import render, redirect, reverse
from django.http import  HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from ipa_board.models import SubPhonemeType, PhonemeType
from .forms import UserRegistrationForm, LoginForm
from .utils import get_all_score, get_sub_phoneme_types,\
    get_filtered_score, get_diphthong_pairs\
    , get_simple_vowels_pairs, get_filtered_vowels_score


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

            return redirect(reverse('ipa_board:index'))

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
    diphthong = SubPhonemeType.objects.get(subtype_name="Diphtongues")
    # all vowels which are not diphthongs are simple vowels, so
    # just one simple vowel subtype is enough
    simple_vowel = SubPhonemeType.objects.get(subtype_name="Pré-fermées")
    # for title location display in template
    if type_id:
        phoneme_type = PhonemeType.objects.get(id=type_id)
    if vowel_type:
        if vowel_type == diphthong.id:
            vowel_subtype = "Diphtongues"
        else:
            vowel_subtype = "Voyelles simples"

    return render(request, 'user/user_score_history.html', locals())


@login_required
def score_chart(request, type_id=None, vowel_type=None):
    """
    Get user score data, takes optional categories
    """
    labels = []
    data = []

    # by default, if no category is chosen, then takes all category
    if not type_id:
        queryset = get_all_score(request)

    else:
        sub_phonemes_types = get_sub_phoneme_types(phoneme_type_id=type_id)

        if not vowel_type:
            queryset = get_filtered_score(request, sub_phonemes_types)

        else:
            vowel_subtype = (SubPhonemeType
                             .objects
                             .get(id=vowel_type))

            if vowel_subtype.subtype_name == "Diphtongues":
                minimal_pairs = get_diphthong_pairs(vowel_subtype)

            else:
                minimal_pairs = get_simple_vowels_pairs()

            queryset = get_filtered_vowels_score(request, minimal_pairs)

    for entry in queryset:
        labels.append(entry['date'])
        data.append(entry['score'])

    # reformat datetime format to DD-MM-YY string
    labels[:] = [date.strftime('%d-%b-%Y') for date in labels]

    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })
