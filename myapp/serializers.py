from rest_framework import serializers
from .models import UserData, Activity

# converting data of Activity model to json
class ActivityPeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ["start_time", "end_time"]

# converting data of user data to json 
class UserSerializer(serializers.ModelSerializer):
    activity_periods = ActivityPeriodSerializer(many=True, read_only=True)

    class Meta:
        model = UserData
        fields = ["id", "real_name", "tz", "activity_periods"]
