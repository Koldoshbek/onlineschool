from django.urls import path

from library.views import *

urlpatterns = [

    path('', LibraryView.as_view(), name='library'),
    path('upload/', AddBookView.as_view(), name='add_book'),

]
