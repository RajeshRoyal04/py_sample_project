from django.db import models

# Create your models here.
class user(models.Model):
	user_id = models.IntegerField(primary_key=True)
	name = models.CharField(max_length=250)
	mobile = models.CharField(max_length=250)
	email = models.CharField(max_length=250)
	password = models.CharField(max_length=250)
	createdon = models.CharField(max_length=250)
def __str__(self):
	return self.name

