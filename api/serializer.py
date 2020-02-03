from rest_framework.serializers import ModelSerializer
from .models import Bucket


class BucketSerializer(ModelSerializer):
    class Meta:
        model = Bucket
        fields = ('id', 'name', 'created_at')
