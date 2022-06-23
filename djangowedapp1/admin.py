from django.contrib import admin
from django.contrib.auth.models import Group
# Register your models here.

from .models import Venue, MyClubUser, Event

# Remove Groups
admin.site.unregister(Group)


#admin.site.register(Venue)
admin.site.register(MyClubUser)
#admin.site.register(Event)


@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone')
    ordering  = ('name',)
    search_fields = ('name',)    
    
    
    
@admin.register(Event)
class EveneAdmin(admin.ModelAdmin):
    fields = (('name', 'venue'),'event_date','description', 'manager')
    list_display = ('name', 'event_date', 'venue' )
    list_filter = ('event_date', 'venue')
    ordering  = ('-event_date', )
    