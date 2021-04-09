#!/bin/sh

# line breaks are in unix format (LF)
coverage run manage.py test ipa_board
coverage run -a manage.py test minimal_pair
coverage run -a manage.py test quiz
coverage run -a manage.py test user
coverage html
