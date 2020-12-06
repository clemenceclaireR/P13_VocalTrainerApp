import urllib
import simpleaudio as sa
from django.shortcuts import render
from . import utils


def minimal_pair(request):
    """
    Display index
    """
    sound_list = utils.read_sound_list("resources/sounds/sound-list.txt")
    print(sound_list)
    return render(request, 'minimal_pair.html', locals())


