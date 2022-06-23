from django.db import models
from django.contrib.auth.models import User 
from datetime import date
# Create your models here.
class Venue(models.Model):
    name = models.CharField("Venue name", max_length=120)
    address = models.CharField( max_length=120)
    zip_code = models.CharField("Zip code", max_length=120)
    phone = models.CharField("Contact number", max_length=120)
    web = models.URLField("Website address")
    email_adress = models.EmailField("Email", max_length=254)
    owner = models.IntegerField("Venue owner", blank=False,default=1)
    image = models.ImageField(null=True, blank=True, upload_to='images/')
    
    
    def __str__(self):
        return self.name
    
class MyClubUser(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField("User email")
    
    def __str__(self):
        return self.first_name + " "+ self.last_name
    
    
    
class Event(models.Model):
    name = models.CharField("Event name", max_length=120)
    event_date = models.DateTimeField("Event date")
    venue = models.ForeignKey(Venue, blank=True, null=True, on_delete=models.CASCADE)
    # venue = models.CharFeild(max_lenght=120)
    # user = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    manager = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    description = models.TextField(blank=True)
    attendees = models.ManyToManyField(MyClubUser)
    
    def __str__(self):
        return self.name


    @property
    def Days_till(self):
        today = date.today()
        days_till = self.event_date.date() - today
        days_till_stripped  = str(days_till).split(',', 1)[0]
        return days_till_stripped

    def till_past(self):
        today = date.today()
        if self.event_date.date() < today:
            thing = "Past"
        else: thing = "Future"
        return thing