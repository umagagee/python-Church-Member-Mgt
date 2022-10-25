from django.shortcuts import render,redirect
from django.http import HttpResponse
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
from .Birthdate import Age
from datetime import date
from .models import *
from .forms import *
# Create your views here.

over = Age()
def index(request):
    member = Member.objects.all()
    payment = Payment.objects.all()
    total_member = Member.objects.all().count()
    total_male = Member.objects.filter(sex="male").count()
    total_female = Member.objects.filter(sex="female").count()

    

    content = {
        "member":member,
        "payment":payment,
        "total_member":total_member,
        "total_male":total_male,
        "total_female":total_female,
    }
    return render(request,"member/index.html",content)

def member(request,pk):
    amt=0.0
    member=Member.objects.get(id=pk)
    payment = Payment.objects.filter(member_id=pk)


    for paid in payment:
        amt += paid.amount

    content = {
        "amt":amt,
        "payment":payment,
        "member":member
    }
    return render(request,"member/member.html",content)

def payment(request):
    form = paymentForm()
    if request.method=='POST':
        form = paymentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    content = {
        "form":form

    }
    return render(request,"member/payment.html",content)

def createMember(request):
    form = memberForm()
    if request.method=='POST':
        form = memberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    
    content = {
        "form":form

    }
    return render(request, "member/create-member.html",content)

def updateMember(request,pk):
    member = Member.objects.get(id=pk)
    form = memberForm(instance = member)
    if request.method =='POST':
        form = memberForm(request.POST, instance = member)
        if form.is_valid():
            form.save()
            return redirect('/')
    content = {
        "form":form

    }
    return render(request, "member/create-member.html",content)

def deleteMember(request,pk):
    delete_member = Member.objects.get(id=pk)
    fullname = delete_member.first_name+" "+delete_member.last_name
    member_id = delete_member.id
    if request.method == 'POST':
        delete_member.delete()
        return redirect('/')
    content ={
        "fullname":fullname,
        "member_id":member_id
    }
    return render(request,"member/delete-member.html",content)

def updatePayment(request,pk):
    update_payment = Payment.objects.get(id=pk)
    form = paymentForm(instance = update_payment)
    if request.method =='POST':
        form = paymentForm(request.POST,instance = update_payment)
        if form.is_valid():
            form.save()
            return redirect('/')
    content = {
            "form":form
        }
    return render(request,"member/payment.html",content)

def deletePayment(request,pk):
    delete_payment = Payment.objects.get(id=pk)
    payment_id = delete_payment.id
    if request.method=='POST':
        delete_payment.delete()
        return redirect('/')
    content={
        "payment_id":payment_id
    }
    return render(request,"member/delete-payment.html",content)

def tyr(request):
    member = Member.objects.all()
    for m in member:
        m = m.birth_date
        num = over.over_age(m)
        
    content = {
        "member":member,
        "num":num
    }

    return render(request,"member/tyr.html",content)