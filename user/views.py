from django.shortcuts import render, redirect
from django.views.generic import TemplateView


class UserProfileView(TemplateView):
    template_name = 'user/profile.html'

    def get(self, request, *args, **kwargs):
        context = {

        }
        return render(request, self.template_name, context)
