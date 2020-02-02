from rest_framework import generics
from .serializer import BucketSerializer
from .models import Bucket

class Buckets(generics.ListCreateAPIView):

    """This class defines the create behavior of our rest api."""

    queryset = Bucket.objects.all()
    serializer_class = BucketSerializer

    def create_bucket(self, serializer):

        """Save the post data when creating a new bucketlist."""

        serializer.save()


