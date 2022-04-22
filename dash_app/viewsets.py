from rest_framework import  viewsets
from rest_framework.response import Response

from .serializer import (
    TypeInfluencerSerializer,
    MarkeSerializer,
    CountrySerializer,
    MediumSerializer,
    CampaignSerializer,
    InfluencerSerializer,
    InfluencerCampaignSerializer
)


from .models import (
            TypeInfluencer, 
            Mark,
            Country,
            Medium,
            Campaign,
            Influencer,
            InfluencerCampaign
            )
# Create your views here.



# class TypeInfluencerViewSet(viewsets.ModelViewSet):
class TypeInfluencerViewSet(viewsets.GenericViewSet):

    """
    This is a influencer type
    """
    queryset = TypeInfluencer.objects.all()
    serializer_class = TypeInfluencerSerializer

    # def list(serlf, request):

    #     return Response({1:1})

class MarkViewSet(viewsets.ModelViewSet):
    queryset = Mark.objects.all()
    serializer_class = MarkeSerializer


class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class MediumViewSet(viewsets.ModelViewSet):
    queryset = Medium.objects.all()
    serializer_class = MediumSerializer


class CampaignViewSet(viewsets.ModelViewSet):
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer



class InfluencerViewSet(viewsets.ModelViewSet):
    queryset = Influencer.objects.all()
    serializer_class = InfluencerSerializer


class InfluencerCampaignViewSet(viewsets.ModelViewSet):
    queryset = InfluencerCampaign.objects.all()
    serializer_class = InfluencerCampaignSerializer