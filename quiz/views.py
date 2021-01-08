from django.shortcuts import render
from django.db.models import DateTimeField, ExpressionWrapper, F
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from minimal_pair.models import MinimalPairInformation
import random


SENT_ANSWERS_LIST = []


# param ici, section
def quiz(request, category_id):
    """
    Renders quiz page.
    Paginates in order to display one question (sound couple) as a time
    """

    # get all the minimal pairs associated to the category sent
    category_id = category_id # in order to send the number to
    all_pairs = MinimalPairInformation.objects.filter(category_id=category_id).values_list('id', flat=True)

    # faire en sorte qu'il ne prenne pas deux fois le même mot
    # pour un mot sur deux, si associated_id = id, kick du queryset (si pas 1/2,va tout supprimer)
    # dans la boucle, si i = pair, garde, sinon, vire

    pairs = MinimalPairInformation.objects.filter(id__in=all_pairs).order_by('id')

    paginator = Paginator(pairs, 1)
    page = request.GET.get('page')
    try:
        questions = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        questions = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        questions = paginator.page(paginator.num_pages)

    return render(request, 'quiz/quiz.html', locals())


# récupérer ici la query à partir du template de quiz => param
def score(request, category_id):
    """
    Display score at the end of the quiz
    """
    score = 0
    all_pairs = MinimalPairInformation.objects.filter(category_id=category_id).values_list('id', flat=True)
    pairs = MinimalPairInformation.objects.filter(id__in=all_pairs).order_by('id')
    temp = []
    for sound_object in pairs:
        temp.append(sound_object.label)

    RIGHT_ANSWERS_LIST = list(dict.fromkeys(temp))
    NEW_SENT_ANSWERS_LIST = list(dict.fromkeys(SENT_ANSWERS_LIST))
    length_list = len(RIGHT_ANSWERS_LIST)
    print('SENT_ANSWERS_LIST ' + str(NEW_SENT_ANSWERS_LIST))
    print('RIGHT_ANSWERS_LIST ' + str(RIGHT_ANSWERS_LIST))
    for i in range(len(SENT_ANSWERS_LIST)):
        print('i = ' + str(i))
        if SENT_ANSWERS_LIST[i] == RIGHT_ANSWERS_LIST[i]:
            score += 1

    # clean at the end of the quiz
    SENT_ANSWERS_LIST.clear()
    return render(request, 'quiz/score.html', locals())


def save_answer(request):

    answer = request.GET['answer']
    SENT_ANSWERS_LIST.append(answer)
    print("SENT_ANSWERS_LIST" + str(SENT_ANSWERS_LIST))

