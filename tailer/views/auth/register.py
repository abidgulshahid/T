import json

from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from django.urls import reverse_lazy, reverse
from django.views import View
from django.contrib.auth import authenticate, login

from tailer.forms.auth import Signup
from tailer.models import Users


class RegisterView(View):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_tailer:
            return HttpResponseRedirect(reverse_lazy('dashboard_view'))
        elif request.user.is_authenticated and request.user.is_superuser:
            admin_url = reverse('admin:index')
            return redirect(admin_url)
        return super(RegisterView, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        # if request.user.is_authenticated:
        #     return HttpResponseRedirect(reverse_lazy('home_view'))
        form = Signup()
        context = {'form': form}
        return render(request, 'tailer/signup.html', context=context)

    def post(self,request):
        form = Signup(data=request.POST)

        if form.is_valid():
            data = form.cleaned_data
            user = form.save(commit=False)
            user.username = data['username']
            user.email = data['username']
            if Users.objects.filter(email__iexact=data['username']).exists():
                print('Already Exists')
            # user.first_name = data['first_name']
            # user.last_name = data['last_name']
            user = form.save()
            user.set_password(user.password)
            user.is_active = False
            user.is_tailer = False
            user.save()
            return HttpResponseRedirect(reverse_lazy('index_view'))
        else:
            print(form.errors)
            context = {'form': form}
            return render(request, 'tailer/signup.html', context=context)
