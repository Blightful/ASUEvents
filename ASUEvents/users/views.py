from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from django.conf import settings
from users.forms import UserForm

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
        uform = UserForm(data=request.POST)
        if uform.is_valid():
            user = uform.save()
            user.set_password(user.password)
            user.save()
            self.registered = True
        else:
            print uform.errors
        context = self.get_context_data()
        context['registered'] = self.registered
        return render(request, self.template_name, context)

    def get(self, request):
        context = self.get_context_data()
        context['uform'] = UserForm()
        context['registered'] = self.registered
        return render(request, self.template_name, context)

