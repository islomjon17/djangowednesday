
import hmac
from django.contrib import admin
from django.urls import path
from djangowedapp1.views import *
urlpatterns = [
    path('', home, name="home"),
    path('<int:year>/<str:month>/', home, name="home" ),
    path('events', all_events, name='list-events'),
    path('add_venue', add_venue, name='add_venue'),
    path('venues_list', venues_list, name='venues_list'),
    path('show_venue/<venue_id>', show_venue, name='show_venue'),
    path('search_menu', search_menu, name='search_menu'),
    path('update_venue/<venue_id>', update_venue, name='update_venue'),
    path('update_event/<event_id>', update_event, name='update_event'), 
    path('add_event', add_event, name='add_event'),
    path('delete_event/<event_id>', delete_event, name='delete_event'), 
    path('delete_venue/<venue_id>', delete_venue, name='delete_venue'), 
    path('venue_text', venue_text, name="venue_text"),
    path('venue_csv', venue_csv, name="venue_csv"),
    path('venue_pdf', pdf_venue, name="venue_pdf"),
    path('my_events', my_events, name="my_events"),
    path('search_events',search_events, name="search_events"),
]
