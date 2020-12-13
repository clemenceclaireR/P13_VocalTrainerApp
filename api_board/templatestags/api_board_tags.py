from django import template

register = template.Library()


@register.filter
def phoneme(phoneme, consonant_title):
    return phoneme.filter(sub_phoneme_type=consonant_title)


@register.filter
def examples(example, phoneme):
    return example.filter(phoneme_id=phoneme)
