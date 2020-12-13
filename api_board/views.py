from django.shortcuts import render
from .models import SubPhonemeType, PhonemeInformation, ExampleWord


def index(request):
    """
    Display index
    """
    return render(request, 'index.html', locals())


def api_board_menu(request):
    """
    Display API board main menu
    """
    return render(request, 'api_board/menu_selection.html', locals())


def consonant_table(request):
    """
    Display consonants
    """
    consonants_type = SubPhonemeType.objects.filter(phoneme_type=1).order_by('subtype_name')
    print(consonants_type)
    phoneme_information = PhonemeInformation.objects.all().order_by('label')
    example_words = ExampleWord.objects.all().order_by('label')
    return render(request, 'api_board/consonant_table.html', locals())
