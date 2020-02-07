from django.urls import path
from .views import Buckets, GetBucketDetail
# from .views import BucketDetails


# app_name = 'bucket'
urlpatterns = [
    path('buckets/', Buckets.as_view(), name="create"),
    path('bucket/<int:bucket_id>', GetBucketDetail.as_view(), name="detail"),
]


