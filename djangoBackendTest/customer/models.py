from django.db import models
from django.core.exceptions import ValidationError

from .validators import validate_phone_number  # validate_first_and_second_name



# Create your models here.
class Customer(models.Model):
    
    CHOICES = (
        ('red', 'Red'),
        ('green', 'Green'),
        ('blue', 'Blue'),
        ('none', 'None'),
    )

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    telephone = models.IntegerField(validators=[validate_phone_number])
    has_purchase_history = models.BooleanField(default=False)
    email = models.EmailField()
    purchase = models.CharField(max_length=250, null=False, choices=CHOICES, default='none')

    def clean(self):
        
        if self.first_name == self.lat_name:
            raise ValidationError('First name and Last cannot be identical!')

    class Meta:
        unique_together = ['first_name', 'last_name', 'email']
