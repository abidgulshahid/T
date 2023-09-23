import json
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth import authenticate, login

from tailer.forms.auth import LoginForm


class LoginView(View):
    def dispatch(self, request, *args, **kwargs):
        return super(LoginView, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        # if request.user.is_authenticated:
        #     return HttpResponseRedirect(reverse_lazy('home_view'))
        form = LoginForm()
        context = {'form': form}
        return render(request, 'tailer/login.html', context=context)