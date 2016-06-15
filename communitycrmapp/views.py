from django.shortcuts import render, render_to_response, HttpResponse
from django.template import RequestContext
from .forms import MemberForm
from .models import Member
from django.core.exceptions import *
import requests
import json
import os

key = os.environ.get("MEETUP_API_KEY")
# Create your views here.

def home(request):
    return render(request, 'communitycrmapp/home.html', {})

def score(request):
    return render(request, 'communitycrmapp/score.html', {})

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

def member_item(request, id):
    member = Member.objects.get(pk=id)
    # meetups pull starts here
    meetup_id = member.meetupid
    r = requests.get("{}{}{}{}".format('https://api.meetup.com/members/', meetup_id, key, '&sign=true&fields=topics'))
    meetups = (r.json()['topics'])
    li = []
    topics = (r.json()['topics'])
    for topic in topics:
        li.append(topic['name'])
    # meetups pull ends here
    return render(request, 'communitycrmapp/member.html', {
        'member': member,
        'meetups': li
    })

def display(request):
    members = Member.objects.all()
    for member in members:
        # meetups pull starts here
        meetup_id = member.meetupid
        r = requests.get("{}{}{}{}".format('https://api.meetup.com/members/', meetup_id, key, '&sign=true&fields=topics'))
        meetups = (r.json()['topics'])
        li = []
        topics = (r.json()['topics'])
        for topic in topics:
            li.append(topic['name'])
        # meetups pull ends here
    return render(request, 'communitycrmapp/display.html', {
        'members': members,
        'meetups': li
    })

def search_by_name(request):
    if request.method == "POST":
        search_id = request.POST.get('namequery')
        try:
            member_by_name = Member.objects.filter(name__icontains= search_id)
            for member in member_by_name:
                # meetups pull starts here
                meetup_id = member.meetupid
                r = requests.get("{}{}{}{}".format('https://api.meetup.com/members/', meetup_id, key, '&sign=true&fields=topics'))
                meetups = (r.json()['topics'])
                li = []
                topics = (r.json()['topics'])
                for topic in topics:
                    li.append(topic['name'])
                # meetups pull ends here
            return render(request, 'communitycrmapp/results.html', {
                'member_by_name': member_by_name,
                'meetups': li})
        except Member.DoesNotExist:
            return HttpResponse("no such user")
    else:
        return render(request, 'communitycrmapp/searchpage.html')

def search_by_volunteer(request):
    if request.method == "POST":
        search_id = request.POST.get('volunteerquery')
        try:
            member_by_volunteer = Member.objects.filter(volunteer__exact= search_id)
            for member in member_by_volunteer:
                # meetups pull starts here
                meetup_id = member.meetupid
                r = requests.get("{}{}{}{}".format('https://api.meetup.com/members/', meetup_id, key, '&sign=true&fields=topics'))
                meetups = (r.json()['topics'])
                li = []
                topics = (r.json()['topics'])
                for topic in topics:
                    li.append(topic['name'])
                # meetups pull ends here
            return render(request, 'communitycrmapp/results.html', {
                'member_by_volunteer': member_by_volunteer,
                'meetups': li
                })
        except Member.DoesNotExist:
            return HttpResponse("no such user")
    else:
        return render(request, 'communitycrmapp/searchpage.html')

def search_by_host(request):
    if request.method == "POST":
        search_id = request.POST.get('hostquery')
        try:
            member_by_host = Member.objects.filter(host__gte= search_id)
            for member in member_by_host:
                # meetups pull starts here
                meetup_id = member.meetupid
                r = requests.get("{}{}{}{}".format('https://api.meetup.com/members/', meetup_id, key, '&sign=true&fields=topics'))
                meetups = (r.json()['topics'])
                li = []
                topics = (r.json()['topics'])
                for topic in topics:
                    li.append(topic['name'])
                # meetups pull ends here
            return render(request, 'communitycrmapp/results.html', {
                'member_by_host': member_by_host,
                'meetups': li})
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
            for member in member_by_fb:
                # meetups pull starts here
                meetup_id = member.meetupid
                r = requests.get("{}{}{}{}".format('https://api.meetup.com/members/', meetup_id, key, '&sign=true&fields=topics'))
                meetups = (r.json()['topics'])
                li = []
                topics = (r.json()['topics'])
                for topic in topics:
                    li.append(topic['name'])
                # meetups pull ends here
            return render(request, 'communitycrmapp/results.html', {
                'member_by_fb': member_by_fb,
                'meetups': li})
        except Member.DoesNotExist:
            return HttpResponse("no such user")
    else:
        return render(request, 'communitycrmapp/searchpage.html')

def donor_search(request):
    if request.method == "POST":
        search_id = request.POST.get('donationquery')
        try:
            donor = Member.objects.filter(donationtotalammount__gte= search_id)
            for member in donor:
                # meetups pull starts here
                meetup_id = member.meetupid
                r = requests.get("{}{}{}{}".format('https://api.meetup.com/members/', meetup_id, key, '&sign=true&fields=topics'))
                meetups = (r.json()['topics'])
                li = []
                topics = (r.json()['topics'])
                for topic in topics:
                    li.append(topic['name'])
                # meetups pull ends here
            return render(request, 'communitycrmapp/results.html', {
                'donor': donor,
                'meetups': li})
        except Member.DoesNotExist:
            return HttpResponse("no such user")
    else:
        return render(request, 'communitycrmapp/searchpage.html')
