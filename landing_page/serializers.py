from rest_framework import serializers
from django.db.models import Avg, ExpressionWrapper, F , Q
from utils.models import City
from announcement.models import Announcement
from feedback.models import *

class CitySerializer(serializers.ModelSerializer):
    rank = serializers.SerializerMethodField('get_rank') 
    class Meta:
        model = City
        fields = ('city_name', 'country', 'c_lat', 'c_long', 'city_small_image64','city_big_image64', 'abbrev_city' , 'area' , 'population',
                    'currency','explore_more','rank')
    def get_rank(self,obj):
        ranks = {}
        cities_query = City.objects.annotate(num_announcements=models.Count('announcement')).order_by('-num_announcements')
        cities_with_images = cities_query.exclude(Q(city_small_image64=None) | Q(city_small_image64=True))
        cities = cities_with_images[:10]
        for i in range(len(cities)):
            if obj == cities[i]:
                return i + 1

class CityRandomshitSerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ('city_name', 'country', 'c_lat', 'c_long', 'city_small_image64','city_big_image64', 'abbrev_city' , 'area' , 'population',
                    'currency','explore_more')

class MostRatedHostSerializer(serializers.ModelSerializer):
    announcer_username = serializers.SerializerMethodField('get_announcer_username') 
    anc_city = serializers.SerializerMethodField('get_anc_city') 
    avg_feedback = serializers.SerializerMethodField('get_avg_feedback') 
    profile_photo = serializers.SerializerMethodField('get_profile_phot') 

    class Meta:
        model = Announcement
        fields = ('id','announcer_username' , 'announcer' ,'anc_city', 'arrival_date','departure_date','travelers_count' , 'profile_photo' 
                ,'avg_feedback')
    
    def get_announcer_username(self,obj):
        return obj.announcer.username,

    def get_anc_city(self,obj):
        return obj.anc_city.city_name

    def get_city_image(self,obj):
        obj.anc_city.city_small_image64

    def get_avg_feedback(self,obj):
        avg_feedbacks = Feedback.objects.values('ans_id__main_host').annotate(
        avg_feedback=Avg(F('question_1') + F('question_2') + F('question_3') + F('question_4') + F('question_5')) / 5)
        max_avg_feedback = avg_feedbacks.order_by('-avg_feedback').first()
        max_avg_feedback_value = max_avg_feedback['avg_feedback']
        announcements = Announcement.objects.filter(main_host=max_avg_feedback['ans_id__main_host'])
        avg_feedback = Feedback.objects.filter(ans_id=obj.id).aggregate(
            avg_feedback=Avg(F('question_1') + F('question_2') + F('question_3') + F('question_4') + F('question_5')) / 5
        )
        return avg_feedback['avg_feedback']
    
    def get_profile_phot(self,obj):
        try:
            return obj.announcer.profile_photo.url
        except Exception as e:
            pass
