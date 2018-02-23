from django.db import models

# Create your models here.
class User(models.Model):
    user_id=models.AutoField(primary_key=True)
    last_name=models.TextField(max_length=30)
    first_name=models.TextField(max_length=30)


class Horse(models.Model):
    horse_id=models.AutoField(primary_key=True)
    horse_name=models.TextField(max_length=20)
    horse_owner=models.TextField(max_length=80)
    horse_club=models.TextField(max_length=30)

class Bet(models.Model):
    bet_id=models.AutoField(primary_key=True)
    bet_price=models.IntegerField()
    bet_multiplier=models.IntegerField()
    bet_user=models.ForeignKey(User)
    bet_horse=models.ForeignKey(Horse)