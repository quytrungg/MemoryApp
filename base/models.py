from django.db import models
from django.contrib.auth.models import User
from mapbox_location_field.models import LocationField
# from mapbox_location_field.forms import LocationField

# Create your models here.
class Memory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    place = models.CharField(max_length=200)
    location = LocationField(map_attrs={
        "center": [20.0, 10.0],
        "marker_color": "blue",
        "marker_size": "medium"
    }, null=True, blank=True)
    memory_name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.memory_name
    
    class Meta:
        ordering = ['complete']
