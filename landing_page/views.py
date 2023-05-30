from django.shortcuts import render
from django.db.models import Avg, ExpressionWrapper, F , Q
from rest_framework.views import APIView
from rest_framework import status , generics
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from announcement.models import Announcement
from feedback.models import Feedback
from accounts.models import *
from .serializers import *
from utils.models import City
import json
from django.http import JsonResponse


class MostRatedHost(APIView):
    def get(self, request):
        avg_feedbacks = Feedback.objects.values('ans_id__main_host').annotate(
            avg_feedback=Avg(F('question_1') + F('question_2') + F('question_3') + F('question_4') + F('question_5')) / 5
        )
        max_avg_feedback = avg_feedbacks.order_by('-avg_feedback').first()
        max_avg_feedback_value = max_avg_feedback['avg_feedback']
        
        announcement_ids = Announcement.objects.filter(
            main_host=max_avg_feedback['ans_id__main_host']
        ).values('id')[:10]
        
        announcement_ids_list = list(announcement_ids)
        filtered_announcements = Announcement.objects.filter(id__in=Subquery(announcement_ids_list))
        
        serializer = MostRatedHostSerializer(filtered_announcements, many=True)
        return Response(serializer.data)

class MostVisitedCities(APIView):
    def get(self,request):
        cities = City.objects.annotate(num_announcements=models.Count('announcement')).order_by('-num_announcements')[:10]
        cities_with_images = cities.exclude(Q(city_small_image64=None) | Q(city_small_image64=True))
        serializer = CitySerializer(cities_with_images, many=True)
        return Response(serializer.data)

class RandomShit(APIView):
    def get(self, request):
        cities = City.objects.exclude(Q(city_big_image64=None) | Q(city_big_image64=True))[:8]
        serializer = CitySerializer(cities, many=True)
        return Response(serializer.data)
