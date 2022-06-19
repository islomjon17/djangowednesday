from asyncio import events
from pickle import NONE
from time import strftime
from urllib import response
from django.shortcuts import render, redirect
import calendar
from django.http import HttpResponseRedirect
from calendar import HTMLCalendar, month
from .models import Event, Venue
#
from django.contrib.auth.models import User
from datetime import datetime
from .form import VenueForm, EventForm, EventFormAmin
from django.http import HttpResponse
import csv
from django.contrib import messages
# import items reportlab


import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter

# import pagnations stuff for odf downloader...

from django.core.paginator import Paginator

# Create your views here.



def my_events(request):
    if request.user.is_authenticated:#### whether loged in or not
        return render(request, 'events/my_events.html', {})
        me = request.user.id
        events = Evvents.objects.filtera(attendees = me)
        return render(request, 'events/my_events.html', {'events': events})
        
    else:
        messages.success(request, ("You are not manager"))
        return redirect ('home ')   







def venue_csv(request):
    if request.user.is_authenticated:#### whether loged in or not
        response = HttpResponse(content_type = "text/csv")
        response['Content-Disposition'] = "attechment; filename=venues.csv"
        # Create a csv writer
        writer = csv.writer(response)
    
        # Designate the model
        venues = Venue.objects.all()
    
    
        # Add column headings to the csv file 
        writer.writerow(['name', 'address', 'zip_code', 'phone', 'web', 'email_adress'])
    
     
        for venue in venues:
            writer.writerow([venue.name, venue.address, venue.zip_code, venue.phone, venue.web, venue.email_adress])
        
   
    
        return response
    else:
        return render(request, "events/eror_401_login.html")
    
    # Write to Text Filie


# Generate Text File Venue List

def venue_text(request):
    if request.user.is_authenticated:#### whether loged in or not
        response = HttpResponse(content_type = "text/plain")
        response['Content-Disposition'] = "attechment; filename=venues.txt"
        # Designate The model
    
        venues = Venue.objects.all()
    
        # Create blank list
        lines = []
        # Loop thu and output
        for venue in venues:
            lines.append(f'{venue.name}\n{venue.address}\n{venue.zip_code}\n{venue.phone}\n{venue.web}\n {venue.email_adress}\n\n\n\n')
        
        # lines = ['This is line 1\n',
        #          "This is line 2\n",
        #          "This is line 3\n"]
        response.writelines(lines)
        return response


    else:
        return render(request, "events/eror_401_login.html")
    
    # Write to Text Filie

#DELETE ITEMES FROM DTABASE

# DELETE EVENT
def delete_event(request, event_id):
    if request.user.is_authenticated:#### whether loged in or not
        event = Event.objects.get(pk=event_id)
        if request.user == event.manager:
            event.delete()
            messages.success(request, ("Event deleted succesfully"))
            return redirect ('list-events')
        else:
            messages.success(request, ("You are not manager"))
            return redirect ('list-events')     
        
    else:
        return render(request, "events/eror_401_login.html")
    


# DELETE VENUE
def delete_venue(request, venue_id):
    if request.user.is_authenticated:#### whether loged in or not
        venue = Venue.objects.get(pk=venue_id)
        venue.delete()
        return redirect ('venues_list')
    else:
        return render(request, "events/eror_401_login.html")


def add_event(request):
    if request.user.is_authenticated:#### whether loged in or not
        submitted=False
        if request.method == 'POST':
            if request.user.is_superuser:
                form = EventFormAmin(request.POST)
                if form.is_valid():
                    form.save()
                    return HttpResponseRedirect('/add_event?submitted=True')
            else:
                form = EventFormAmin(request.POST)
                if form.is_valid():
                    # form.save()
                    event = form.save(commit=False)
                    event.manager = request.user
                    event.save()

                    return HttpResponseRedirect('/add_event?submitted=True')
        else:
            if request.user.is_superuser:
                form = EventFormAmin
            else:
                form = EventForm
            if 'submitted' in  request.GET:
                submitted=True 
        return render(request, "events/add_event.html", {'form' : form, 'submitted': submitted} )
    else:
        return render(request, "events/eror_401_login.html")







def search_menu(request):
    
    if request.method == "POST":
        searched = request.POST['searched']
        venues = Venue.objects.filter(name__contains = searched)
        return render(request, 'events/search_venues.html' , {'searched':searched, 'venues':venues} )

    else:
        return render(request, 'events/search_venues.html', {})




def update_venue(request, venue_id):
    if request.user.is_authenticated:#### whether loged in or not
        venue = Venue.objects.get(pk=venue_id)
        form = VenueForm(request.POST or None, instance=venue)  
        if form.is_valid():
                form.save()
                return redirect('venues_list')
        
        return render(request, "events/update_venue.html", {'venue':venue, 'form':form})
    else:
        return render(request, "events/eror_401_login.html")

def update_event(request, event_id):
#    if request.user.is_authenticated:#### whether loged in or not
        event = Event.objects.get(pk=event_id)
        if request.user.is_superuser:
            form = EventForm(request.POST or None, instance=event) 
        else:
            form = EventForm(request.POST or None, instance=event)  
        if form.is_valid():
                form.save()
                return redirect('list-events')

        return render(request, "events/update_event.html", {'event':event, 'form':form})
#    else:
#        return render(request, "events/eror_401_login.html")



def venues_list(request):
    #venues_list = Venue.objects.all().order_by('name')
    venues_list = Venue.objects.all()
    #Set up pagination
    p = Paginator(Venue.objects.all(), 1)
    page = request.GET.get('page')
    venues = p.get_page(page)
    nums = "a" * venues.paginator.num_pages
    
    return render(request, "events/venue.html", 
        {'venues_list':venues_list,
        "venues":venues,
        "nums":nums}
        )
    


def show_venue(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)
    venue_owner = User.objects.get(pk=venue.owner)

    return render(request, "events/show_venue.html", 
        {'venue':venue,
        'venue_owner' : venue_owner})
    



def add_venue(request):
    if request.user.is_authenticated:#### whether loged in or not
        submitted=False
        if request.method == 'POST':
            form = VenueForm(request.POST)
            if form.is_valid():
                venue = form.save(commit=False)
                venue.owner = request.user.id
                venue.save()
                return HttpResponseRedirect('/add_venue?submitted=True')
        else:
            form = VenueForm
            if 'submitted' in  request.GET:
                submitted=True 
        return render(request, "events/add_venue.html", {'form' : form, 'submitted': submitted} )
    else:
        return render(request, "events/eror_401_login.html")



def home(request, year=datetime.now().year, month=datetime.now().strftime("%B")):
    # Convert month from  name to number
    month = month.capitalize( )
    month_number = list(calendar.month_name).index(month)
    month_number = int(month_number)
    
    #create calendar
    
    cal = HTMLCalendar().formatmonth(
        year,
        month_number
    )
    
    now = datetime.now()
    current_year = now.year
    
    # Get current time
    time = now.strftime("%H:%M %p")
    
    return render(request, 
        'events/home.html', {
            
            "year":year,
            "month":month,     
            "month_number": month_number ,   
            "cal":cal,  
            "current_year":current_year,
            "time":time,
            }) 
    
    
def all_events(request):
    event_list = Event.objects.all().order_by('event_date')
    return render(request, "events/events_list.html", 
                  {'event_list':event_list})
    
    
    
def pdf_venue(request):
    if request.user.is_authenticated:#### whether loged in or not
        # create bytestream buffer
    
        buf = io.BytesIO()

        # Create a Canvas 
        c = canvas.Canvas(buf, pagesize=letter, bottomup=0 )
        # Crreate a text object
        textob = c.beginText()
        textob.setTextOrigin(inch, inch)
        textob.setFont("Helvetica", 14)
    
    
        # Add some lines of text
        # lines = [
        #     "This is line 1",
        #     "This is line 2",
        #     "This is line 3",
        
        
        # ]
    
    
        venues = Venue.objects.all()
        lines = []
        for venue in venues:
            lines.append(venue.name)
            lines.append(venue.address),
            lines.append(venue.zip_code),
            lines.append(venue.phone),  
            lines.append(venue.web),
            lines.append(venue.email_adress), 
            lines.append("  "),    
        # iter.writerow([venue.name, venue.address, venue.zip_code, venue.phone, venue.web, venue.email_adress])
    
        # loop
    
        for line in lines:
            textob.textLine(line)
    
    
        # Finish up
    
        c.drawText(textob)
        c.showPage()
        c.save()
        buf.seek(0)
    
    
        # Return 
    
        return FileResponse(buf, as_attachment=True, filename = "venue.pdf")
    else:
        return render(request, "events/eror_401_login.html")
    


