import random
from django.contrib import messages
from django.views.decorators.cache import never_cache
from django.http import JsonResponse
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from minimal_pair.models import MinimalPairInformation, MinimalPairCategory
from ipa_board.models import SubPhonemeType, PhonemeType
from quiz.models import Score


@never_cache
def quiz(request, category_id):
    """
    Renders quiz page.
    Paginates in order to display one question (sound couple) as a time
    """
    page = request.GET.get('page')
    print(request.path_info)

    # get all the minimal pairs associated to the category sent
    category_id = category_id  # in order to send the number to

    all_pairs = MinimalPairInformation.objects.filter(category_id=category_id) \
        .values_list('id', flat=True)

    # takes only 8 sounds randomly only when quiz is at the beginning
    # in order to avoid the query to be executed each time

    if page is None:
        random_sound_list = random.sample(list(all_pairs), min(len(all_pairs), 8))

        quiz_query_randomized = MinimalPairInformation.objects.filter \
            (id__in=random_sound_list)

        # store a random value in order to mix the query
        random_val = random.random()

        request.session['quiz_query'] = sorted(quiz_query_randomized.values(),
                                               key=lambda x: random_val)

    try:
        paginator = Paginator(request.session['quiz_query'], 1)
    except KeyError:
        return HttpResponseRedirect(request.path_info + "?page=" + request.GET.get("page", '1'))

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
    request.session['score'] = 0
    category_id = category_id

    # for template breadcrumbs
    category = MinimalPairCategory.objects.get(id=category_id)
    phoneme_category = SubPhonemeType.objects.get(id=category.sub_phoneme_type_id.id)
    parent_category = PhonemeType.objects.get(id=phoneme_category.phoneme_type_id)

    # retrieve quiz answers label
    quiz_answers_label = []
    for sound_object in request.session['quiz_query']:
        quiz_answers_label.append(sound_object['label'])

    right_answers_list = list(dict.fromkeys(quiz_answers_label))

    # retrieve answers and pages sent by user
    user_sent_data = request.session["user_answers_list"]
    user_answers_label = []
    for data_dict in user_sent_data:
        user_answers_label.append(data_dict['answer'])

    length_list = len(right_answers_list)
    # print('sent data' + str(user_answers_label))
    # print('right_answers_list ' + str(right_answers_list))

    # check answers integrity and increment user score
    keep_one_answer_per_page(request, user_answers_label, right_answers_list)

    # for display in template
    score = request.session['score']
    return render(request, 'quiz/score.html', locals())


def keep_one_answer_per_page(request, user_data, original_data):
    """
    Iterates through dict in order to check if
    an answer has not been sent multiple time to
    the same page. If an answer has already
    been given to a page, it is not kept.
    """
    for i in range(len(user_data)):
        try:
            if user_data[i] == original_data[i]:
                request.session['score'] += 1
        except IndexError:
            message = messages.add_message(request, messages.ERROR,
                                           'Une erreur est survenue lors de l\'enregistreme,t'
                                           'des résultats.')
            return message


def save_answer(request):
    """
    Get user answer from Ajax and store in into list
    Each answer is associated with its page in order
    to get one answer per page.
    """
    if request.method == 'POST':

        answer = request.POST.get('answer')
        page = request.POST.get('page')

        # answer_by_page = {'answer': answer, 'page': page}
        answers_by_page_list = []
        answers_by_page_list.append({'answer': answer, 'page': page})
        request.session["user_answers_list"] = \
            request.session["user_answers_list"][:]\
            + answers_by_page_list.copy()
        # print(request.session["user_answers_list"])

        sent_answers_list = request.session["user_answers_list"]
        pages_number_list = []
        for data_dict in sent_answers_list:
            if not data_dict['page'] in pages_number_list:
                pages_number_list.append(data_dict['page'])
            else:
                sent_answers_list.remove(data_dict)

        response = JsonResponse(request.POST.get('answer'), safe=False)
        return response


@login_required
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
