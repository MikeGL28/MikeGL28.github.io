from rest_framework.serializers import ModelSerializer
from .models import URL


class URLSerializer(ModelSerializer):
    class Meta:
        model = URL
        fields = ['title', 'full_url', 'short_url', 'pub_data']
