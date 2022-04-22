from rest_framework import serializers



from .models import (
            TypeInfluencer, 
            Mark,
            Country,
            Medium,
            Campaign,
            Influencer,
            InfluencerCampaign
            )

class TypeInfluencerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model= TypeInfluencer
        fields='__all__'


class MarkeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model= Mark
        fields='__all__'

class CountrySerializer(serializers.ModelSerializer):
    
    class Meta:
        model= Country
        fields='__all__'


class MediumSerializer(serializers.ModelSerializer):
    
    class Meta:
        model= Medium
        fields='__all__'


class CampaignSerializer(serializers.ModelSerializer):
    
    class Meta:
        model= Campaign
        fields='__all__'


class InfluencerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model= Influencer
        fields='__all__'



class InfluencerCampaignSerializer(serializers.ModelSerializer):
    
    class Meta:
        model= InfluencerCampaign
        fields='__all__'