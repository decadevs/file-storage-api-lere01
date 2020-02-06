from rest_framework.serializers import ModelSerializer
from .models import Bucket


class BucketSerializer(ModelSerializer):
    class Meta:
        model = Bucket
        fields = '__all__'

    def create(self, validated_data):
        return Bucket.objects.create(**validated_data)
