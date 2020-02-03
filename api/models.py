from django.db import models

# Create your models here.
class Bucket(models.Model):
    name = models.CharField(max_length = 200, blank = False, unique = True)
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.name)