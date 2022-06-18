from cProfile import label
from logging import PlaceHolder
# from msilib.schema import Control
from turtle import textinput
from django import forms
from django.forms import ModelForm
from .models import Venue, Event

class VenueForm(ModelForm):
    class Meta:
        model = Venue
        fields = ['name','address','zip_code', 'phone', 'web', 'email_adress']
        labels = {
            'name':  '',
           'address': ''
            ,'zip_code': ''
            , 'phone':''
            , 'web': ''
            , 'email_adress': '',
            
        }
        
        widgets = {
            
           'name':  forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Name'}),
           'address': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Address' })
            ,'zip_code':forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Zip code'})
            , 'phone':forms.TextInput(attrs={'class':'form-control', 'placeholder': 'phone'})
            , 'web':forms.TextInput(attrs={'class':'form-control', 'placeholder': 'web'})
            , 'email_adress': forms.EmailInput(attrs={'class':'form-control', 'placeholder': 'Email address'}),
        }
        
        
# Admin super User event form
class EventFormAmin(ModelForm):
    class Meta:
        model = Event
        fields = ['name','event_date','venue', 'manager', 'attendees', 'description']
        labels = {
            'name':  '',
           'event_date': 'YYYY-MM-DD HH-MM-SS'
            ,'venue': 'venue'
            , 'manager': 'manager',
            'attendees': 'attendees',
            'description': '',
             
            
        }
        
        widgets = {
            
           'name':  forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Name'}),
           'event_date': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'event_date' })
            ,'venue':forms.Select(attrs={'class':'form-select', 'placeholder': 'venue'})
            , 'manager':forms.Select(attrs={'class':'form-select', 'placeholder': 'manager'})
            , 'attendees': forms.SelectMultiple(attrs={'class':'form-control', 'placeholder': 'attendees'})
            , 'description':forms.Textarea(attrs={'class':'form-control', 'placeholder': 'description'})
            
            
        }





#User event form
class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ['name','event_date','venue', 'attendees', 'description']
        labels = {
            'name':  '',
           'event_date': 'YYYY-MM-DD HH-MM-SS'
            ,'venue': 'venue',
            'attendees': 'attendees',
            'description': '',
             
             
        }
        
        widgets = {
            
           'name':  forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Name'}),
           'event_date': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'event_date' })
            ,'venue':forms.Select(attrs={'class':'form-select', 'placeholder': 'venue'})
            
            , 'attendees': forms.SelectMultiple(attrs={'class':'form-control', 'placeholder': 'attendees'})
            , 'description':forms.Textarea(attrs={'class':'form-control', 'placeholder': 'description'})
            
            
        }