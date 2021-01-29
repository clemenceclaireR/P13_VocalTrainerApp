from django import template
from minimal_pair.models import MinimalPairWordPhonemePlace, MinimalPairInformation

register = template.Library()


@register.filter(name='zip')
def zip_lists(a, b):
    return zip(a, b)


@register.filter()
def get_associated_sound_id(sound_id):
    """
    Returns words phoneme letters
    """
    sound = MinimalPairInformation.objects.get(id=sound_id)
    return sound.label
