from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.urls import reverse
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth import logout
from django.db.models import Q
from tailer.forms.tailor_form import TailorForm
from tailer.models import Customer, RequestAccess


class Dashboard(View):
    def dispatch(self, request, *args, **kwargs):
        return super(Dashboard, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        form = TailorForm()
        if 'get_list' in request.GET:
            search = request.GET.get('search')
            get_tailers = ""

            if request.user.is_tailer:
                get_tailers = Customer.objects.filter(tailer=request.user)
            else:
                get_tailers = Customer.objects.filter(user_id=request.user.id)
            if search: get_tailers =  get_tailers.filter(Q(name__icontains=search) | Q(phone_number__icontains=search))
            context = {'get_tailers': get_tailers}
            string = render(request, 'tailer/_partial/_list.html', context=context)
            return HttpResponse(string)
        if 'obj' in request.GET:
            get_obj = request.GET.get('obj')
            obj = Customer.objects.filter(id=get_obj, user_id=request.user.id).first()
            edit_form = TailorForm(instance=obj)
            context = {'entry_form': edit_form, 'obj': obj}
            string = render(request, 'tailer/_partial/_edit.html', context=context)
            return HttpResponse(string)
        if 'delete_id' in request.GET:
            delete_id = request.GET.get('delete_id')
            obj = Customer.objects.filter(id=delete_id, user_id=request.user.id).first()
            obj.delete()
            return HttpResponse('success')
        if 'request_id' in request.GET:
            get_obj = Customer.objects.filter(id=request.GET.get('request_id')).first()
            if get_obj:
                get_obj.request_access = True
                RequestAccess.objects.create(requested_by_id= request.user.id, requested_to_id = get_obj.user_id, record_number=request.GET.get('request_id') )
                get_obj.save()
                return HttpResponse('success')

        if 'approve' in request.GET:
            get_obj = Customer.objects.filter(id=request.GET.get('approve')).first()
            if get_obj:
                get_obj.request_access = False
                get_obj.is_approved = True
                RequestAccess.objects.create(is_approved = True,requested_by_id= request.user.id, requested_to_id = get_obj.user_id, record_number=request.GET.get('approve') )
                get_obj.save()
                return HttpResponse('success')

        return render(request, 'tailer/dashboard.html', context={'request': request, 'entry_form': form})

    def post(self, request):
        print(request.POST)

        if 'create_entry' in request.POST:
            form = TailorForm(data=request.POST)
            if form.is_valid():
                data = form.cleaned_data
                obj = form.save(commit=False)
                obj.user = request.user
                if request.user.is_user:
                    obj.tailer = data['tailer']
                else:
                    obj.tailer = request.user
                obj.save()
                return HttpResponse('success')
            print(form.errors)
            return render(request, 'tailer/_partial/_create.html', context={'request': request, 'entry_form': form})

        if 'edit_entry' in request.POST:
            edit_entry = request.POST.get('edit_entry')
            edit_form = TailorForm(instance=Customer.objects.filter(user_id=request.user.id, id=edit_entry).first(),
                                   data=request.POST)
            if edit_form.is_valid():
                obj = edit_form.save(commit=False)
                obj.user_id = request.user.id
                print('hello world')
                obj.save()
                return HttpResponse('success')
            print(edit_form.errors, 'error')
            return render(request, 'tailer/_partial/_edit.html', context={'request': request, 'entry_form': edit_form})





class DataView(View):
    def dispatch(self, request, *args, **kwargs):
        return super(DataView, self).dispatch(request, *args, **kwargs)

    def get(self, request,id):
        get_data = get_object_or_404(Customer, user=request.user, id=id)
        print(get_data, 'get data')
        return render(request, 'tailer/view_detail.html', context={'request': request, 'get_data':get_data})


'''This View will logout the user'''
class LogoutView(View):
    def dispatch(self, request, *args, **kwargs):
        return super(LogoutView, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse_lazy('index_view'))
