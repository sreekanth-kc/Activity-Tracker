import uuid
from django.db import models


class Users(models.Model):
    """
    Class Name: User
    Description: Manages user details.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    real_name = models.CharField(max_length=20, blank=False)
    time_zone = models.CharField(max_length=100, blank=False)

    class Meta:
        db_table = 'user_details'


class ActivityPeriod(models.Model):
    """
    class Name: ActivityPeriod
    Description: Manage user activities.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    user = models.ForeignKey(Users, on_delete=models.CASCADE)

    class Meta:
        db_table = 'user_activities'
