from rest_framework import serializers
from .models import pclog

class pclogserializers(serializers.ModelSerializer):

    class Meta:
        model = pclog
        fields = ['date', 'pc', 'ip', 'user', 'app_name', 'app_title', 'open_time']