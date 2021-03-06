"""vocal_trainer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('minimal_pair.urls', namespace='minimal_pair')),
    path('', include('quiz.urls', namespace='quiz')),
    path('', include('ipa_board.urls', namespace='ipa__board')),
    path('', include('user.urls', namespace='user')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# in order to not raise django.urls.exceptions.NoReverseMatch: 'djdt' is not a registered namespace while testing
if settings.DEBUG or settings.TESTING_MODE:
    import debug_toolbar

    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
    # urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
