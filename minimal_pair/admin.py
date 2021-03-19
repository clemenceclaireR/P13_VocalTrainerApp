from django.contrib import admin
from .models import MinimalPairInformation, MinimalPairCategory, MinimalPairWordPhonemeLetters

admin.site.register(MinimalPairInformation)
admin.site.register(MinimalPairCategory)
admin.site.register(MinimalPairWordPhonemeLetters)
