from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.urls import reverse
from django.shortcuts import redirect

from tailer.forms.tailor_form import TailorForm
from tailer.models import Tailor


class Dashboard(View):
    def dispatch(self, request, *args, **kwargs):
        return super(Dashboard, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        form = TailorForm()
        if request.user.is_authenticated:
            if 'get_list' in request.GET:
                get_tailers = Tailor.objects.filter(user_id=request.user.id)
                context = {'get_tailers': get_tailers}
                string = render(request, 'tailer/_partial/_list.html', context=context)
                return HttpResponse(string)
            if 'obj' in request.GET:
                get_obj = request.GET.get('obj')
                obj = Tailor.objects.filter(id=get_obj, user_id=request.user.id).first()
                edit_form  =TailorForm(instance=obj)
                context =  {'entry_form': edit_form}
                string = render(request, 'tailer/_partial/_edit.html', context=context)
                return HttpResponse(string)
            return render(request, 'tailer/dashboard.html', context={'request':request, 'entry_form':form})
        return HttpResponseRedirect(reverse_lazy('index_view'))

    def post(self, request):
        print(request.POST)

        if 'create_entry' in request.POST:
            form = TailorForm(data=request.POST)
            if form.is_valid():
                data = form.cleaned_data
                obj = form.save(commit=False)
                obj.user = request.user
                obj.save()
                return HttpResponse('success')
            print(form.errors)
            return render(request, 'tailer/_partial/_create.html', context={'request': request, 'entry_form': form})

        if 'edit_entry' in request.POST:
            edit_entry = request.POST.get('edit_entry')
            edit_form = TailorForm(instance=Tailor.objects.filter(user_id=request.user.id, id=edit_entry))
            if edit_form.is_valid():
                edit_form.save()
                return HttpResponse("success")
            return render(request, 'tailer/_partial/_edit.html', context={'request': request, 'entry_form': edit_form})