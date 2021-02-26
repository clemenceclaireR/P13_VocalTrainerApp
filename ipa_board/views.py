from django.shortcuts import render
from .models import SubPhonemeType, PhonemeInformation, ExampleWord


def index(request):
    """
    Display index
    """
    return render(request, 'index.html', locals())


def ipa_board_menu(request):
    """
    Display API board main menu
    """
    return render(request, 'ipa_board/menu_selection.html', locals())


def consonant_table(request):
    """
    Display consonants
    """
    consonants_type = (SubPhonemeType.objects.filter(phoneme_type=1)
                       .order_by('order'))
    phoneme_information = (PhonemeInformation.objects.all()
                           .order_by('id'))
    example_words = (ExampleWord.objects.all()
                     .order_by('label'))

    return render(request, 'ipa_board/consonant_table.html',
                  locals())


def vowels_type_menu(request):
    """
    Display vowels menu
    """
    return render(request, 'ipa_board/vowel_menu.html', locals())


def diphthong_table(request):
    """
    Display diphthong vowels
    """

    vowels = PhonemeInformation.objects.filter(sub_phoneme_type=11)
    example_words = (ExampleWord.objects.all()
                     .order_by('label'))

    return render(request, 'ipa_board/diphthong_table.html',
                  locals())


def simple_vowel_table(request):
    """
    Display vowels
    """
    vowels_type = ['Pré-fermées', 'Fermées', 'Semi-ouvertes'
        , 'Ouvertes', 'Moyennes']
    sub_phoneme_types_ids = (SubPhonemeType.objects
                             .filter(subtype_name__in=vowels_type)
                             .values_list('id', flat=True))

    vowels = (PhonemeInformation.objects
              .filter(sub_phoneme_type__in=sub_phoneme_types_ids))

    example_words = (ExampleWord.objects.all()
                     .order_by('label'))

    return render(request, 'ipa_board/simple_vowel_table.html', locals())
