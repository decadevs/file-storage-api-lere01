from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import BucketSerializer
from .models import Bucket


# class Buckets(APIView):
#     def get(self, request):
#         buckets = Bucket.object.all()
#         return Response({ buckets })


class Buckets(generics.ListCreateAPIView):

    queryset = Bucket.objects.all()
    serializer_class = BucketSerializer

    def create_bucket(self, serializer):
        serializer.save()


class BucketDetails(generics.RetrieveUpdateDestroyAPIView):

    queryset = Bucket.objects.all()
    serializer_class = BucketSerializer
