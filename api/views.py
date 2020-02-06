from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import BucketSerializer
from .models import Bucket
from django.shortcuts import get_object_or_404
from rest_framework import status


class Buckets(APIView):

    def get(self, request, format='json'):
        buckets = Bucket.objects.all()
        serializer = BucketSerializer(buckets, many=True)
        return Response(serializer.data)

    def post(self, request, format='json'):
        bucket = request.data

        serializer = BucketSerializer(data=bucket)

        if serializer.is_valid(raise_exception=True):
            bucket_saved = serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)

        return Response(serializer.errors, status.HTTP_400_BAD_RESQUEST)


class GetBucketDetail(APIView):
    """
    Retrieve, update or delete a bucket instance.
    """
    def get_object(self, bucket_id):

        try:
            return Bucket.objects.get(pk = bucket_id)

        except Bucket.DoesNotExist:
            return Response(status = status.HTTP_400_BAD_REQUEST)

    def get(self, request, bucket_id):

        # using request .data because its an API not form
        bucket_detail = self.get_object(bucket_id)

        #serializer object for edit created
        serializers = BucketSerializer(bucket_detail)

        return Response(serializers.data, status = status.HTTP_200_OK)



    def put(self, request, bucket_id, format='json'):

        # using request .data because its an API not form
        data = request.data

        bucket_detail = self.get_object(bucket_id)

        #serializer object for edit created
        serializers = BucketSerializer(bucket_detail, data)

        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status = status.HTTP_200_OK)

        return Response(serializers.errors, status = status.HTTP_400_BAD_REQUEST)

    def delete(self, request, bucket_id):
        bucket = self.get_object(bucket_id)
        bucket.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)


# class Buckets(generics.ListCreateAPIView):

#     queryset = Bucket.objects.all()
#     serializer_class = BucketSerializer

#     def create_bucket(self, serializer):
#         serializer.save()


# class BucketDetails(generics.RetrieveUpdateDestroyAPIView):

#     queryset = Bucket.objects.all()
#     serializer_class = BucketSerializer
