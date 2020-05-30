import json
from django.core.management.base import BaseCommand
from user_activity.models import Users, ActivityPeriod


class Command(BaseCommand):
    """
    Class Name: Command
    Description: Load table with dummy data.
    """
    def add_arguments(self, parser):
        parser.add_argument('user', type=str)
        parser.add_argument('activity', type=str)

    def handle(self, *args, **options):
        with open(options['user']) as f:
            users_list = json.load(f)
        with open(options['activity']) as f:
            activity_list = json.load(f)

        for user in users_list:
            user['pk'] = user.pop('pk')
            Users.objects.get_or_create(pk=user['pk'], defaults=user)
        for activity in activity_list:
            activity['user'] = Users.objects.get(id=activity['user'])
            activity['pk'] = activity.pop('pk')
            ActivityPeriod.objects.get_or_create(pk=activity['pk'], defaults=activity)