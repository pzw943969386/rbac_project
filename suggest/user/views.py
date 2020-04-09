from django.shortcuts import render,redirect
from django.conf import settings
from django.views import View

# Create your views here.

class LoginView(View):

    def get(self,request):
        return render(request,'user/login.html')

    def post(self,request):
        username = request.POST.get('username')
        password = request.POST.get('password')

