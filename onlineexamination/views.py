from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import TemplateView

from onlineexamination.models import Exams


class ExamsView(LoginRequiredMixin, TemplateView):
    template_name = 'onlineexamination/add_exam.html'

    def get(self, request, *args, **kwargs):
        exams = Exams.objects.all()
        context = {
            'exams': exams,

        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        context = {

        }
        return render(request, self.template_name, context)
