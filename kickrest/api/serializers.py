from rest_framework import serializers
from api.models import Cham

class KickSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cham
        fields = ('backers_count','blurb','catergory','converted','created_at','id')
