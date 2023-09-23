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

    def post(self,request):
        print('reqest', 'here')
        form = LoginForm(data=request.POST)
        if form.is_valid():
            print()
            data = form.cleaned_data
            print(data)
            auth = authenticate(**data)
            print(auth, 'auth')
            if auth:
                login(request,auth)
                return HttpResponseRedirect(reverse_lazy('dashboard_view'))
            return HttpResponseRedirect(reverse_lazy('index_view'))
        print(form.errors)