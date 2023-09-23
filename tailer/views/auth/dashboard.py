from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.urls import reverse
from django.shortcuts import redirect


class Dashboard(View):
    def dispatch(self, request, *args, **kwargs):
        return super(Dashboard, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        form = ''
        if request.user.is_authenticated:
            if 'get_list' in request.GET:
                context = {}
                string = render(request, 'tailer/_partial/_list.html', context=context)
                return HttpResponse(string)
            return render(request, 'tailer/dashboard.html', context={'request':request, 'form':form})
        return HttpResponseRedirect(reverse_lazy('index_view'))

    def post(self, request):
        print(request.POST)
        # form = PaymentForm(data=request.POST)
        # if 'create_entry' in request.POST:
        #     if form.is_valid():
        #         data = form.save(commit=False)
        #         data.user_id = request.user.id
        #         data.save()
        #         return HttpResponse("success")