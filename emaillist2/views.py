from django.shortcuts import render
from django.http import HttpResponseRedirect
from emaillist2.models import Emaillist2

# Create your views here.
def index(request):

    emaillist2 = Emaillist2.objects.all().order_by('-id')
    return render(request, 'emaillist2/index.html',{'emaillist2_list':emaillist2})


def form(request):
    return render(request, 'emaillist2/form.html')

def add(request):
    emaillist2 = Emaillist2()
    emaillist2.first_name = request.POST['fn']
    emaillist2.last_name = request.POST['ln']
    emaillist2.email = request.POST['email']

    emaillist2.save()

    return HttpResponseRedirect('/emaillist2')