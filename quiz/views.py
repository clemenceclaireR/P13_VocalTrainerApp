import random
import json
import time
from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render, redirect, reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from minimal_pair.models import MinimalPairInformation, MinimalPairCategory
from api_board.models import SubPhonemeType, PhonemeType
from quiz.models import Score
from django.core.cache import cache


def quiz(request, category_id):
    """
    Renders quiz page.
    Paginates in order to display one question (sound couple) as a time
    """

    page = request.GET.get('page')

    # get all the minimal pairs associated to the category sent
    category_id = category_id  # in order to send the number to

    all_pairs = MinimalPairInformation.objects.filter(category_id=category_id) \
        .values_list('id', flat=True)

    # takes only 8 sounds randomly only when quiz is at the beginning
    # in order to avoid the query to be executed everytime

    if page is None:
        random_sound_list = random.sample(list(all_pairs), min(len(all_pairs), 8))

        quiz_query_randomized = MinimalPairInformation.objects.filter \
            (id__in=random_sound_list)

        # store a random value in order to mix the query
        random_val = random.random()

        request.session['ORIGINAL_QUIZ_QUERY'] = sorted(quiz_query_randomized.values(),
                                     key=lambda x: random_val)

    paginator = Paginator(request.session['ORIGINAL_QUIZ_QUERY'], 1)

    try:
        questions = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        questions = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        questions = paginator.page(paginator.num_pages)

    return render(request, 'quiz/quiz.html', locals())


def score(request, category_id):
    """
    Display score at the end of the quiz
    """
    # wait for save answer function to finish its job
    time.sleep(1)
    request.session['score'] = 0
    category_id = category_id

    # for template breadcrumbs
    category = MinimalPairCategory.objects.get(id=category_id)
    phoneme_category = SubPhonemeType.objects.get(id=category.sub_phoneme_type_id.id)
    parent_category = PhonemeType.objects.get(id=phoneme_category.phoneme_type_id)

    answers_label = []

    for sound_object in request.session['ORIGINAL_QUIZ_QUERY']:
        answers_label.append(sound_object['label'])

    right_answers_list = list(dict.fromkeys(answers_label))
    sent_answers_list = request.session["SENT_ANSWER_LIST"]
    length_list = len(right_answers_list)
    print('sent_answer_list ' + str(sent_answers_list))
    print('right_answers_list ' + str(right_answers_list))
    for i in range(len(sent_answers_list)):
        if sent_answers_list[i] == right_answers_list[i]:
            request.session['score'] += 1

    # for display in template
    score = request.session['score']
    return render(request, 'quiz/score.html', locals())


@csrf_exempt
def save_answer(request):
    """
    Get user answer from Ajax and store in into list
    """
    if request.method == 'POST':

        print(request.POST.get('answer'))
        answer = request.POST.get('answer')
        request.session["SENT_ANSWER_LIST"] += [answer]
        print(request.session["SENT_ANSWER_LIST"])
        response = JsonResponse(request.POST.get('answer'), safe=False)
        return response


def save_results(request, category_id):
    """
    Store user result with associated minimal
    pair category and current datetime
    """
    Score.objects.create(
        score=request.session['score']
        , user_id=User.objects.get(id=request.user.id)
        , minimal_pair_category_id=MinimalPairCategory.objects.get(id=category_id)
    )
    return redirect(reverse('user:user_score_history'))
