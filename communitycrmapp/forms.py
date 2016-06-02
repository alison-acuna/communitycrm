from django import forms

from .models import Member

class MemberForm(forms.ModelForm):

    class Meta:
        model = Member
        fields = ('name','number', 'email', 'fbpagelink', 'address', 'meetuplink',
        'polynteer', 'eventshosted', 'eventshostedname', 'ohb', 'ohbcontributions',
        'launchteam', 'launchteamcontributions', 'fbgroupmember', 'donationtotalammount',
            )
