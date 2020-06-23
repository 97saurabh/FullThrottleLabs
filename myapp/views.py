from django.shortcuts import render
from . import forms, models
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer
from django.views.generic import CreateView
from django.http import JsonResponse
import json
# Homepage
def home(request):

    return render(request, "myapp/base.html", {})

# Api Call for displaying data
class ArticalAPIView(APIView):
    def get(self, request):
        articles = models.UserData.objects.all()
        serializer = UserSerializer(articles, many=True)
        data_member = {"ok": "true", "members": serializer.data}

        

        data_member = json.dumps(data_member, indent = 4)



        json_object = json.loads(data_member)

        json_formatted_str = json.dumps(json_object, indent=4)

        return JsonResponse(json_object,safe=False)

# For Adding data to user model
class UserCreateView(CreateView):

    form_class = forms.UserForm
    model = models.UserData

# for adding data to user model
class ActivityCreateView(CreateView):

    form_class = forms.ActivityForm
    model = models.Activity
