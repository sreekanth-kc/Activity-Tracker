from rest_framework import serializers
from user_activity.models import Users, ActivityPeriod


class UserActivitySerializer(serializers.ModelSerializer):
    """
    Class Name: UserActivitySerializer.

    Description: Serializer class for get user log details.
    """
    activity_period = serializers.SerializerMethodField()

    class Meta:
        model = Users
        fields = ('id', 'real_name', 'time_zone', 'activity_period')

    @classmethod
    def get_activity_period(cls, obj):
        """

        :param obj:
        :return:
        """
        activity_list = []
        activities = ActivityPeriod.objects.filter(user=obj.id)
        for activity in activities:
            time = {"start_time": activity.start_time.strftime("%B %d %Y %I:%M %p"),
                    "end_time": activity.end_time.strftime("%B %d %Y %I:%M %p")}
            activity_list.append(time)
        return activity_list
