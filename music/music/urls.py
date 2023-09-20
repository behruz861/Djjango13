from django.contrib import admin
from django.urls import path, include

import music1.views
import music2.views
import music3.views
from music1.views import show_jazz, start_page
from music2.views import show_rok, start_page
from music3.views import show_pop, start_page


urlpatterns = [
    path('', start_page),
    path('music/jazz/', music1.views.show_jazz),
    path("music/", include("music1.urls")),

    path('music/rok/', music2.views.show_rok),
    path('music/', include('music2.urls')),

    path('music/pop/', music3.views.show_pop),
    path('music/', include('music3.urls')),

    path('admin/', admin.site.urls),
]
