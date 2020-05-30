"""
File Name: views.py

Description: Define views for user_activity module.
"""
from rest_framework.views import APIView
from utils.mixins import HttpResponseMixin
from user_activity.models import Users
from user_activity.serializers import UserActivitySerializer
from django.http import HttpResponse




def home_page(request):
    html = "<html><body>Please try this API <b>https://user-activity-tracker.uc.r.appspot.com/getuseractivity</b> in Post Man for getting the activity results</body></html>"
    return HttpResponse(html)


class UserActivities(APIView, HttpResponseMixin):
    """
    Class Name: UserActivities
    Description : Get user activity details.

    """
    def get(self, request):
        """
        Function Name: post

        Description: Return Response and JWT if authentication is success.

        Input:
            param request: HTTP Request

        Output:
            Formatted json consist of user activity details.
        """
        if request.method == 'GET':
            try:
                users = Users.objects.all()
                serializer = UserActivitySerializer(users, many=True)
                response = serializer.data

                return self.success_response(data=response,
                                             code='HTTP_200_OK',
                                             message="Success")
            except Exception as e:
                return self.error_response(code='HTTP_400_BAD_REQUEST',
                                           message=str(e))
