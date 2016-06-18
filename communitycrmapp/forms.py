from django import forms

from .models import Member

class MemberForm(forms.ModelForm):
    """
    renames a variety of model columns for user interaction
    """

    meetupid = forms.CharField(label='Meetup ID')
    eventshostedname = forms.CharField(label='Events Hosted')
    ohbcontributions = forms.IntegerField(label='Open Heart Brigade Participation')
    ohb = forms.NullBooleanField(label="Open Heart Brigade")
    launchteam = forms.NullBooleanField(label="Launch Team")
    launchteamcontributions = forms.IntegerField(label="Launch Team Contributions")
    fbgroupmember = forms.NullBooleanField(label="Facebook Group Member")
    fbpagelink = forms.URLField(label="Facebook Page Link")
    donationtotalammount = forms.IntegerField(label="Donation Ammount")

    class Meta:
        model = Member
        fields = ('name', 'email', 'address', 'phone', 'volunteer', 'host',
        'launchteam', 'launchteamcontributions', 'fbgroupmember', 'fbpagelink',
        'donationtotalammount', 'ohb', 'ohbcontributions', 'eventshostedname', 'meetupid'
        )
