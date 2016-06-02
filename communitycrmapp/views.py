from django.shortcuts import render, render_to_response, HttpResponse
from django.template import RequestContext
from .forms import MemberForm
from .models import Member
from django.core.exceptions import *

# Create your views here.

def home(request):
    return render(request, 'communitycrmapp/home.html', {})

def searchpage(request):
    return render(request, 'communitycrmapp/searchpage.html', {})

def new(request):
    if request.method == "POST":
        form = MemberForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return render(request, 'communitycrmapp/success.html', {'form': form})
    else:
        form = MemberForm()
    return render(request, 'communitycrmapp/new.html', {'form': form})

def display(request):
    members = Member.objects.all()
    return render(request, 'communitycrmapp/display.html', {
        'members': members
    })

def member_item(request, id):
    member = Member.objects.get(pk=id)
    return render(request, 'communitycrmapp/member.html', {
        'member': member
    })

def search_by_name(request):
    if request.method == "POST":
        search_id = request.POST.get('namequery')
        try:
            member_by_name = Member.objects.filter(name__icontains= search_id)
            print(member_by_name)
            return render(request, 'communitycrmapp/results.html', {
                'member_by_name': member_by_name})
        except Member.DoesNotExist:
            return HttpResponse("no such user")
    else:
        return render(request, 'communitycrmapp/searchpage.html')

def search_by_volunteer(request):
    if request.method == "POST":
        search_id = request.POST.get('volunteerquery')
        try:
            member_by_volunteer = Member.objects.filter(polynteer__exact= search_id)
            return render(request, 'communitycrmapp/results.html', {
                'member_by_volunteer': member_by_volunteer})
        except Member.DoesNotExist:
            return HttpResponse("no such user")
    else:
        return render(request, 'communitycrmapp/searchpage.html')

def search_by_host(request):
    if request.method == "POST":
        search_id = request.POST.get('hostquery')
        try:
            member_by_host = Member.objects.filter(eventshosted__gte= search_id)
            return render(request, 'communitycrmapp/results.html', {
                'member_by_host': member_by_host})
        except Member.DoesNotExist:
            return HttpResponse("no such user")
    else:
        return render(request, 'communitycrmapp/searchpage.html')

def search_by_ohb(request):
    if request.method == "POST":
        search_id = request.POST.get('ohbquery')
        try:
            member_by_ohb = Member.objects.filter(ohb__exact= search_id)
            return render(request, 'communitycrmapp/results.html', {
                'member_by_ohb': member_by_ohb})
        except Member.DoesNotExist:
            return HttpResponse("no such user")
    else:
        return render(request, 'communitycrmapp/searchpage.html')

def search_by_lt(request):
    if request.method == "POST":
        search_id = request.POST.get('ltquery')
        try:
            member_by_lt = Member.objects.filter(launchteam__exact= search_id)
            return render(request, 'communitycrmapp/results.html', {
                'member_by_lt': member_by_lt})
        except Member.DoesNotExist:
            return HttpResponse("no such user")
    else:
        return render(request, 'communitycrmapp/searchpage.html')

def search_by_fb(request):
    if request.method == "POST":
        search_id = request.POST.get('fbquery')
        try:
            member_by_fb = Member.objects.filter(fbgroupmember__exact= search_id)
            return render(request, 'communitycrmapp/results.html', {
                'member_by_fb': member_by_fb})
        except Member.DoesNotExist:
            return HttpResponse("no such user")
    else:
        return render(request, 'communitycrmapp/searchpage.html')

def donor_search(request):
    if request.method == "POST":
        search_id = request.POST.get('donationquery')
        try:
            donor = Member.objects.filter(donationtotalammount__gte= search_id)
            return render(request, 'communitycrmapp/results.html', {
                'donor': donor})
        except Member.DoesNotExist:
            return HttpResponse("no such user")
    else:
        return render(request, 'communitycrmapp/searchpage.html')
