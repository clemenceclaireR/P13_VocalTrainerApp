from django.shortcuts import render
from ipa_board.models import SubPhonemeType, PhonemeType
from .models import MinimalPairCategory, MinimalPairInformation


def minimal_pair_menu(request):
    """
    Display minimal pair category menu
    """
    return render(request, 'minimal_pair/minimal_pair_menu.html'
                  , locals())


def minimal_pair_consonant_menu(request):
    """
    Display page where user choose a type of minimal
    pair belonging to the consonants category
    """
    consonant_type = PhonemeType.objects.get(type_name="Consonnes")
    consonants_subtypes = (SubPhonemeType.objects
                           .filter(phoneme_type=consonant_type.id)
                           .values_list('id', flat=True))

    minimal_pairs = (MinimalPairCategory.objects
                     .filter(sub_phoneme_type_id__in=consonants_subtypes))

    return render(request, 'minimal_pair/minimal_pair_consonant_menu.html'
                  , locals())


def minimal_pair_vowels_type_menu(request):
    """
    Display vowels menu
    """
    return render(request, 'minimal_pair/minimal_pair_vowel_menu.html'
                  , locals())


def minimal_pair_diphthong_menu(request):
    """
    Display page where user choose a type of
    minimal pair belonging to the diphthong category
    """
    diphthong_type = SubPhonemeType.objects.get(subtype_name="Diphtongues")
    minimal_pairs = (MinimalPairCategory.objects
                     .filter(sub_phoneme_type_id=diphthong_type.id))

    return render(request, 'minimal_pair/minimal_pair_diphthong_menu.html'
                  , locals())


def minimal_pair_simple_vowel_menu(request):
    """
    Display page where user choose a type of
    minimal pair belonging to the simple vowel category
    """
    vowel_type = PhonemeType.objects.get(type_name="Voyelles")
    simple_vowel_types = (SubPhonemeType.objects
                           .filter(phoneme_type=vowel_type.id)
                           .values_list('id', flat=True)
                          .exclude(subtype_name="Diphtongues"))
    minimal_pairs = (MinimalPairCategory.objects
                     .filter(sub_phoneme_type_id__in=simple_vowel_types))

    return render(request, 'minimal_pair/minimal_pair_simple_vowel_menu.html'
                  , locals())


def minimal_pair_table(request, phoneme):
    """
    Display minimal pairs associated to
    given phoneme
    """
    category = MinimalPairCategory.objects.get(id=phoneme)

    phoneme_category = (SubPhonemeType.objects
                        .get(id=category.sub_phoneme_type_id.id))

    parent_category = (PhonemeType.objects
                       .get(id=phoneme_category.phoneme_type_id))

    minimal_pairs = (MinimalPairInformation.objects
                     .filter(category_id=phoneme)
                     .order_by('id'))

    return render(request, 'minimal_pair/minimal_pair_table.html'
                  , locals())
