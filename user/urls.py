from django.urls import path

from user.views import *

urlpatterns = [

    path('profile/', UserProfileView.as_view(), name='profile'),

]
