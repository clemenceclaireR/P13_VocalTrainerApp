from quiz.views import QuizData


class CleanQuizAnswerMiddleware:
    """
    If user interrupts quiz, clean its answers
    when he arrives on any other views other than quiz view
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        current_url = str(request.path)
        # these views are the only one working with quiz answers
        list_view_can_keep_score_list = ['quiz', 'answer', 'score']
        # if url does not contains quiz url keywords, then the user answers are cleared
        if not any(ext in current_url for ext in list_view_can_keep_score_list):
            print('SENT ANSWER LIST BEFORE CLEAN ' + str(QuizData.SENT_ANSWERS_LIST))
            QuizData.SENT_ANSWERS_LIST.clear()
            print('DONE')

        response = self.get_response(request)
        return response
