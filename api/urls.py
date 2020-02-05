from django.urls import path
# from rest_framework.urlpatterns import format_suffix_patterns
from .views import Buckets
from .views import BucketDetails

# app_name = 'bucket'
urlpatterns = [
    path('', Buckets.as_view(), name="create"),
    path('bucket/<int:pk>', BucketDetails.as_view(), name="detail"),
]
