from django import template
from minimal_pair.models import MinimalPairWordPhonemeLetters, MinimalPairInformation

register = template.Library()


@register.filter
def check_if_label_exists(phoneme):
    """
    If associated phoneme is null, returns null sign; otherwise, returns its label
    """
    try:
        return phoneme.label
    except AttributeError:
        return '∅'


@register.filter
def get_phoneme_letters(label_id):
    """
    Returns words phoneme letters
    """
    sound = MinimalPairInformation.objects.get(id=label_id)
    phoneme_letters = MinimalPairWordPhonemeLetters.objects.get(minimal_pair_id=sound.id)
    return phoneme_letters.letters


@register.filter
def get_phoneme_ipa_letters(label_id):
    """
    Returns words international phonetic alphabet phoneme letters
    """
    sound = MinimalPairInformation.objects.get(id=label_id)
    phoneme_letters = MinimalPairWordPhonemeLetters.objects.get(minimal_pair_id=sound.id)
    return phoneme_letters.ipa_letters
