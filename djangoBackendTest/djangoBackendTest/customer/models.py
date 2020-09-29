from django.db import models

from .validators import validate_phone_number  # validate_first_and_second_name


# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50, validators=[])
    telephone = models.IntegerField(validators=[validate_phone_number])
    isCustomersWhoMadePurchase = models.BooleanField(default=False)
    # purchase = models.CharField(max_length=30, default='', blank=True )
    email = models.EmailField()
    ###
    CHOICES = (
        ('red', 'Red'),
        ('green', 'Green'),
        ('blue', 'Blue'),
        ('none', 'None'),
    )

    purchase = models.CharField(max_length=250, null=False, choices=CHOICES, default='none')

    ###

    def clean(self):
        from django.core.exceptions import ValidationError
        if self.first_name == self.second_name:
            raise ValidationError('First name and Second are the same text!')
        if self.isCustomersWhoMadePurchase == True and self.purchase == 'none':
            raise ValidationError('Choose car color in "Purchase"')
        if self.isCustomersWhoMadePurchase == False and self.purchase != 'none':
            raise ValidationError('Remember to check "IsCustomersWhoMadePurchase" when You picked car color')

    class Meta:
        unique_together = ['first_name', 'second_name', 'email']
