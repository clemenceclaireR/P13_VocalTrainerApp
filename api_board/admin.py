from django.contrib import admin
from .models import PhonemeType, PhonemeInformation, SubPhonemeType, ExampleWord

admin.site.register(PhonemeType)
admin.site.register(PhonemeInformation)
admin.site.register(SubPhonemeType)
admin.site.register(ExampleWord)
