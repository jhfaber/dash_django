# from django.shortcuts import get_object_or_404, render

# Create your views here.

# from django.urls import path

# from . import views

# from .models import Element, Category,TypeElement

# from django.urls import path, include
# from django.contrib.auth.models import User

from rest_framework import routers
from rest_framework.decorators import action
from rest_framework.response import Response


from .viewsets import (
    TypeInfluencerViewSet,
    MarkViewSet,
    CountryViewSet,
    MediumViewSet,
    CampaignViewSet,
    InfluencerViewSet,
    InfluencerCampaignViewSet

)








router =routers.SimpleRouter()
router.register(r'typeinfluencer',TypeInfluencerViewSet)
router.register(r'mark',MarkViewSet)
router.register(r'country',CountryViewSet)
router.register(r'medium',MediumViewSet)
router.register(r'campaign',CampaignViewSet)
router.register(r'influencer',InfluencerViewSet)
router.register(r'influencercampaign',InfluencerCampaignViewSet)


urlpatterns = router.urls
# app_name = 'rest_api'

# urlpatterns = [
#     path('', include(router.urls)),
#     # path('rest_api/', include('rest_api.urls', namespace='rest_framework'))
# ]