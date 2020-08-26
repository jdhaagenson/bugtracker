from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class CustomUser(AbstractUser):
    pass
# TODO: Write custom user


# TODO Tickets:
#      fields: title, time/date filed, description,
#              name of user who filed, status of ticket,
#              name of user assigned to ticket, name of user who completed
#      new tickets should have status=new, user assigned=None, user who filed: logged in user

