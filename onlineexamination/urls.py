from django.urls import path

from onlineexamination.views import ExamsView

urlpatterns = [

    path('', ExamsView.as_view(), name='exams'),

]