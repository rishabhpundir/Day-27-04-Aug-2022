from django import forms
from django.forms import ModelForm
from ClubApp.models import Event

# Create an EVent form to add data to DB Event
class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = "__all__"          # OR            fields = ("event_name", "event_date", "venue", "event_manager", "event_creator", "description", "venue_image")

        labels = {
            'event_name' :  "",
            'event_date' :  "",
            'venue' :  "",
            'event_manager' :  "",
            'event_creator' :  "",
            'description' : "",
        }

        widgets = {
            'event_name' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Event Name'}),
            'event_date' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Event Date (YYYY-MM-DD HH:MM:SS)'}),
            'venue' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Venue Address'}),
            'event_manager' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Event Manager'}),
            'event_creator' : forms.TextInput(attrs={'class':'form-control', 'value':'<ENTER YOUR USERNAME HERE>'}),
            'description' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Description'}),
        }
        