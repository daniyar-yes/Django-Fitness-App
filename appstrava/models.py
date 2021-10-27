import datetime

from django.db import models
from django.utils import timezone
from datetime import datetime


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=30)
    def __str__(self):
        return self.name

SPORT_TYPES = (
    ('Pull-ups', 'PULL-UPS'),
    ('Push-ups', 'PUSH-UPS'),
    ('Crunches', 'CRUNCHES'),
    ('Squats', 'SQUATS'),
)


class Record(models.Model):
    sport_type = models.CharField(max_length=10, choices=SPORT_TYPES, default='Pull-ups')
    pub_date = models.DateTimeField('date posted')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.PositiveSmallIntegerField(default=0)
    #likes = models.PositiveSmallIntegerField(default=0)  
    def user_str(self):
        return str(self.user)
    def __str__(self):
        return self.sport_type
    def was_posted_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def record_name(self):
        return (str(self.user) + ' did ' +  str(self.amount) + ' ' + str(self.sport_type) + ' on ' + str(self.pub_date.strftime("%d/%m/%Y")))
# add classes for Top (records by month, day, sports);
# add class for Feed that shows 20 last records posted by friends only
# add Friend List class that contains names of Users who are in friends
# add likes behaviour