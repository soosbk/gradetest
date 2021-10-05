from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.db import models
from main.models import UserModel

# Create your views here.

count_num = 0
participation=0



def main(request):
    global count_num
    global participation
    count_num=0
    participation+=1
    return render(request, 'main.html', {'participation': participation})



def test(request):  #1 로 이동

    return render(request, 'test1.html')

def test1(request): #2로 이동
    global count_num
    if(request.method == 'POST'):
        count_n = request.POST['answer']
        count_num += int(count_n)
    return render(request, 'test2.html', {'count': count_num})

def test2(request): #3로 이동
    global count_num
    if(request.method == 'POST'):
        count_n = request.POST['answer']
        count_num += int(count_n)
    return render(request, 'test3.html')




def test3(request):
    global count_num
    if(request.method == 'POST'):
        count_n = request.POST['answer']
        count_num += int(count_n)
    return render(request, 'test4.html')

def test4(request):
    global count_num
    if(request.method == 'POST'):
        count_n = request.POST['answer']
        count_num += int(count_n)
    return render(request, 'test5.html')


def test5(request):
    global count_num
    if(request.method == 'POST'):
        count_n = request.POST['answer']
        count_num += int(count_n)
    return render(request, 'test6.html')


def test6(request):
    global count_num
    if(request.method == 'POST'):
        count_n = request.POST['answer']
        count_num += int(count_n)
    return render(request, 'test7.html')


def test7(request):
    global count_num
    if(request.method == 'POST'):
        count_n = request.POST['answer']
        count_num += int(count_n)
    
    return render(request, 'test8.html')


def result(request):
    global count_num
    if(request.method == 'POST'):
        count_n = request.POST['answer']
        count_num += int(count_n)
        user = UserModel()
        user.count_num = count_num

        if user.count_num == 7:
            return render(request, 'F.html')
        elif user.count_num <=9:
            return render(request, 'D0.html')
        elif user.count_num == 10:
            return render(request, 'D+.html')
        elif user.count_num == 11:
            return render(request, 'C0.html')
        elif user.count_num == 12:
            return render(request, 'C+.html')
        elif user.count_num == 13:
            return render(request, 'B0.html')
        elif user.count_num == 14:
            return render(request, 'B+.html')
        elif user.count_num <=16:
            return render(request, 'A0.html')
        else:
            return render(request, 'A+.html')
    

