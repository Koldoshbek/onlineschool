from django.shortcuts import render
from django.views.generic import TemplateView


class ProfileView(TemplateView):
    template_name = 'user/profile.html'

    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        context = {}
        return render(request, self.template_name, context)
