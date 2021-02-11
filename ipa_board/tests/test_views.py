from django.test import TestCase
from django.urls import reverse
from minimal_pair.models import MinimalPairCategory, MinimalPairInformation
from ipa_board.models import SubPhonemeType, PhonemeType, PhonemeInformation


class IPABoardTest(TestCase):
    """

    """

    def test_index_is_accessible(self):
        """
        Index page returns success http request
        """
        response = self.client.post(reverse("ipa_board:index"))
        self.assertTrue(response.status_code, 200)
