import locale

from django.db.models import Q
from quiz.models import Score
from minimal_pair.models import MinimalPairCategory
from ipa_board.models import SubPhonemeType, PhonemeType


def get_all_score(request):
    """
    Get user score from all categories
    """
    queryset = (Score.objects.values('score', 'date')
                .filter(user_id=request.user)
                .order_by('date'))
    return queryset


def get_sub_phoneme_types(phoneme_type_id):
    """
    Get subtypes groups for vowels or consonant type
    """
    phoneme_type = (PhonemeType
                    .objects
                    .get(id=phoneme_type_id))

    sub_phonemes_types = (SubPhonemeType
                          .objects
                          .values_list('id', flat=True)
                          .filter(phoneme_type_id=phoneme_type.id))

    return sub_phonemes_types


def get_filtered_score(request, sub_phoneme_list):
    """
    Get score for consonants or vowel subtypes
    """
    minimal_pairs = (MinimalPairCategory
                     .objects
                     .values_list('id', flat=True)
                     .filter(sub_phoneme_type_id__in=sub_phoneme_list))
    queryset = (Score
                .objects
                .values('score', 'date')
                .filter(Q(user_id=request.user) &
                        Q(minimal_pair_category_id_id__in=minimal_pairs))
                .order_by('date'))

    return queryset


def get_diphthong_pairs(vowel_subtype):
    """
    Get diphthongs minimal pairs
    """
    minimal_pairs = (MinimalPairCategory
                     .objects
                     .values_list('id', flat=True)
                     .filter(sub_phoneme_type_id=vowel_subtype.id))

    return minimal_pairs


def get_simple_vowels_pairs():
    """
    Get simple vowels minimal pairs
    """
    vowel_type = (PhonemeType
                  .objects
                  .get(type_name="Voyelles"))

    simple_vowels = (SubPhonemeType
                     .objects
                     .values_list('id', flat=True)
                     .filter(phoneme_type_id=vowel_type.id)
                     .exclude(subtype_name="Diphtongues"))

    minimal_pairs = (MinimalPairCategory
                     .objects
                     .values_list('id', flat=True)
                     .filter(sub_phoneme_type_id__in=simple_vowels))

    return minimal_pairs


def get_filtered_vowels_score(request, minimal_pairs):
    """
    Get user score filtered by vowel
    subtype (simple vowels or diphthong)
    """
    queryset = (Score
                .objects
                .values('score', 'date')
                .filter(Q(user_id=request.user) &
                        Q(minimal_pair_category_id__in=minimal_pairs))
                .order_by('date'))
    return queryset


def set_local_variable():
    """
    Try to get french locale in OS, else get default set one
    """
    try:
        locale.setlocale(locale.LC_ALL, 'fr_FR')
    except Exception as e:
        locale.setlocale(locale.LC_ALL, '')
