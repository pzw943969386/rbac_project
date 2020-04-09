from django.shortcuts import render,redirect
from django.core.paginator import Paginator


def shouye(request):

    return render(request,'shouye.html')