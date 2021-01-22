from django import template

register = template.Library()


@register.filter
def class_phoneme(phoneme, consonant_title):
    """
    Get phonemes corresponding to given category
    """
    return phoneme.filter(sub_phoneme_type=consonant_title)


@register.filter
def examples(example, phoneme):
    """
    Get examples associated to the phoneme
    """
    return example.filter(phoneme_id=phoneme)
