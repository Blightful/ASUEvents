from django.shortcuts import render
from django.views.generic import TemplateView
from django.conf import settings
from managers.forms import ManagerForm

import os


class RegisterView(TemplateView):

    def __init__(self):
        self.template_name = os.path.join(settings.TEMPLATE_PATH, 'register.html')
        self.context = {
            'title': '',
            'subtitle': '',
            'addfonts': [

            ],
            'addstyles': [

            ],
            'addscripts': [

            ]
        }
        self.registered = False

    def get_context_data(self):
        return self.context

    def post(self, request):
        context = self.get_context_data()
        mform = ManagerForm(data=request.POST)
        if mform.is_valid():
            profile = mform.save(commit=False)
            profile.save()
            self.registered = True
        else:
            context['mform'] = mform
            return render(request, self.template_name, context)
        context['registered'] = self.registered
        return render(request, self.template_name, context)

    def get(self, request):
        context = self.get_context_data()
        context['mform'] = ManagerForm()
        context['registered'] = self.registered
        return render(request, self.template_name, context)