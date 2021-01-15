from django.shortcuts import render
from django.db import models
from django.db.models import DateTimeField, ExpressionWrapper, F
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from minimal_pair.models import MinimalPairInformation
import random


class QuizData:
    SENT_ANSWERS_LIST = []
    QUIZ_QUERY = []
    RANDOM_SOUND_LIST = []


def quiz(request, category_id):
    """
    Renders quiz page.
    Paginates in order to display one question (sound couple) as a time
    """
    page = request.GET.get('page')
    print('PAGE ' +str(page))
    # get all the minimal pairs associated to the category sent
    category_id = category_id # in order to send the number to
    all_pairs = MinimalPairInformation.objects.filter(category_id=category_id).values_list('id', flat=True)

    # takes only 8 sounds randomly only when quiz is at the beginning
    # in order to avoid the query to be executed everytime
    if page is None:
        QuizData.RANDOM_SOUND_LIST = random.sample(list(all_pairs), min(len(all_pairs), 8))
        QuizData.QUIZ_QUERY = MinimalPairInformation.objects.filter(id__in=QuizData.RANDOM_SOUND_LIST)

        # mixes the ids in order to sounds to be shuffled
        QuizData.QUIZ_QUERY = sorted(QuizData.QUIZ_QUERY.order_by('id'), key=lambda x: random.random())

    paginator = Paginator(QuizData.QUIZ_QUERY, 1)

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

    temp = []
    for sound_object in QuizData.QUIZ_QUERY:
        temp.append(sound_object.label)

    RIGHT_ANSWERS_LIST = list(dict.fromkeys(temp))
    NEW_SENT_ANSWERS_LIST = QuizData.SENT_ANSWERS_LIST
    length_list = len(RIGHT_ANSWERS_LIST)
    print('SENT_ANSWERS_LIST ' + str(NEW_SENT_ANSWERS_LIST))
    print('RIGHT_ANSWERS_LIST ' + str(RIGHT_ANSWERS_LIST))
    for i in range(len(QuizData.SENT_ANSWERS_LIST)):
        print('i = ' + str(i))
        if QuizData.SENT_ANSWERS_LIST[i] == RIGHT_ANSWERS_LIST[i]:
            score += 1

    # clean at the end of the quiz
    QuizData.SENT_ANSWERS_LIST.clear()
    return render(request, 'quiz/score.html', locals())


def save_answer(request):
    answer = request.GET['answer']
    QuizData.SENT_ANSWERS_LIST.append(answer)
    print("SENT_ANSWERS_LIST" + str(QuizData.SENT_ANSWERS_LIST))

