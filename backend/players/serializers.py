from rest_framework import serializers
from .models import Player


class PlayerSerializer(serializers.ModelSerializer):
    
    url = serializers.HyperlinkedIdentityField(view_name='player-detail')
    estimated_price_by_year = serializers.SerializerMethodField(read_only=True)
    
    
    class Meta:
        model = Player
        fields = ['pk','name', 'sports', 'estimated_price','url','estimated_price_by_year']
        # lookup_field = 'pk'
        
        
    def get_estimated_price_by_year(self,obj):
        return f"{obj.estimated_price * 12} Million $"