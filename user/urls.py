from django.urls import path

from user.views import *

urlpatterns = [

    path('profile/', UserProfileView.as_view(), name='profile'),
    path('', LoginRequest.as_view(), name='login'),
    path('logout/', LogoutRequest.as_view(), name='logout'),

]
