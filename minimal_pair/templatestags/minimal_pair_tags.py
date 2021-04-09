from django import template

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

