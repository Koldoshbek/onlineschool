from django.urls import path

from library.views import LibraryView

urlpatterns = [

    path('', LibraryView.as_view(), name='library'),
]
