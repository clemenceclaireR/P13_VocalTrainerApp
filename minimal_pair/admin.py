from django.contrib import admin
from .models import MinimalPairInformation, MinimalPairCategory, MinimalPairWordPhonemePlace

admin.site.register(MinimalPairInformation)
admin.site.register(MinimalPairCategory)
admin.site.register(MinimalPairWordPhonemePlace)

