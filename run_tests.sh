#!/bin/sh

# this script needs to be set in unix encoding for linebreaks if run on linux
coverage run manage.py test ipa_board
coverage run -a manage.py test minimal_pair
coverage run -a manage.py test quiz
coverage run -a manage.py test user
coverage html
