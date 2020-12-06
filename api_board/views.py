from django.shortcuts import render


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


def consonant_menu(request):
    """
    Display consonants
    """
    return render(request, 'api_board/consonant_menu.html', locals())