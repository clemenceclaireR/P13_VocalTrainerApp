from django import template
from minimal_pair.models import MinimalPairInformation

register = template.Library()


@register.filter(name='zip')
def zip_lists(first_list, second_list):
    """
    Aggregates both lists in a tuple
    """
    return zip(first_list, second_list)


@register.filter()
def get_associated_sound_id(sound_id):
    """
    Returns words phoneme letters
    """
    sound = MinimalPairInformation.objects.get(id=sound_id)
    return sound.label
