import urllib
from django.shortcuts import render
from django.db.models import Window, F
from django.db.models.functions import Lead
from . import utils
from .models import MinimalPairCategory, MinimalPairInformation
from api_board.models import SubPhonemeType, PhonemeType


def minimal_pair_menu(request):
    """
    Display minimal pair category menu
    """
    return render(request, 'minimal_pair/minimal_pair_menu.html', locals())


def minimal_pair_consonant_menu(request):
    """
    Display page where user choose a type of minimal pair belonging to the consonants category
    """
    consonants_type = SubPhonemeType.objects.filter(phoneme_type=1).values_list('id', flat=True)
    minimal_pairs = MinimalPairCategory.objects.filter(sub_phoneme_type_id__in=consonants_type)
    return render(request, 'minimal_pair/minimal_pair_submenu.html', locals())


def minimal_pair_diphthong_menu(request):
    """
    Display page where user choose a type of minimal pair belonging to the diphthong category
    """
    diphthong_type = SubPhonemeType.objects.get(id=11)
    minimal_pairs = MinimalPairCategory.objects.filter(sub_phoneme_type_id=diphthong_type.id)
    return render(request, 'minimal_pair/minimal_pair_submenu.html', locals())


def minimal_pair_table(request, phoneme):
    """
    Display minimal pairs associated to given phoneme
    """

    category = MinimalPairCategory.objects.get(id=phoneme)
    phoneme_category = SubPhonemeType.objects.get(id=category.sub_phoneme_type_id.id)
    parent_category = PhonemeType.objects.get(id=phoneme_category.phoneme_type_id)

    # phoneme_category = SubPhonemeType.objects.get(id=phoneme).subphoneme_type_id
    minimal_pairs = MinimalPairInformation.objects.filter(category_id=phoneme).order_by('id')

    return render(request, 'minimal_pair/minimal_pair_table.html', locals())



