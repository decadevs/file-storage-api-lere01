from django.urls import path
# from rest_framework.urlpatterns import format_suffix_patterns
from .views import Buckets

urlpatterns = [
    path('buckets/', Buckets.as_view(), name="create"),
]


