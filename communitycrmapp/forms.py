from django import forms

from .models import Member

class MemberForm(forms.ModelForm):

    meetupid = forms.CharField(label='Meetup ID')
    eventshostedname = forms.CharField(label='Events Hosted')
    ohbcontributions = forms.IntegerField(label='Open Heart Brigade Participation')
    ohb = forms.NullBooleanField(label="Open Heart Brigade")

    class Meta:
        model = Member
        fields = ('name', 'email', 'address', 'phone', 'volunteer', 'host',
        'launchteam', 'launchteamcontributions', 'fbgroupmember', 'fbpagelink',
        'donationtotalammount', 'ohb', 'ohbcontributions', 'eventshostedname', 'meetupid'
        )
