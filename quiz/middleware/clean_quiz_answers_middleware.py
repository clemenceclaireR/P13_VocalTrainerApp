from django.contrib.sessions.middleware import SessionMiddleware
import random
import json
import time
from django.core import serializers
from django.http import JsonResponse
from minimal_pair.models import MinimalPairInformation, MinimalPairCategory


class CleanQuizAnswerMiddleware(SessionMiddleware):
    """
    If user interrupts quiz, clean its answers
    when he arrives on any other views other than quiz view
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        current_url = str(request.path)
        # these views are the only one working with quiz answers
        list_view_can_keep_score_list = ['quiz', 'answer', 'score', 'save']
        # if url does not contains quiz url keywords, then the user answers are cleared
        if not any(ext in current_url for ext in list_view_can_keep_score_list):
            request.session["SENT_ANSWER_LIST"] = []
            request.session['ORIGINAL_QUIZ_QUERY'] = []
            request.session['score'] = None

        response = self.get_response(request)
        return response


