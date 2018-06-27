from django.shortcuts import render
from emaillist.models import Emaillist
from django.http import HttpResponseRedirect

# Create your views here.
def index(request): # handler 함수 django가 실행시킴
    #emaillist 객체가 로우가 list형태로 들어감
    emaillist_list = Emaillist.objects.all().order_by('-id')  #테이블 모든 데이터 id로 desc로 정렬해서 가져와라
    data ={'emaillist_list':emaillist_list}
    return render(request,'index.html', data)  #결과 html을 브라우저에 리턴
    
def form(request):
    return render(request, 'form.html')  # 결과 html을 브라우저에 리턴
    
def add(request):
    emaillist = Emaillist()
    emaillist.first_name = request.POST['fn']# param POST 에 dictionary로 들어있다
    emaillist.last_name = request.POST['ln']
    emaillist.email = request.POST['email']
    
    emaillist.save() # db에 저장하라

    return HttpResponseRedirect('/emaillist')
   # return render(request, 'success.html') #응답리턴



    
    
    
    