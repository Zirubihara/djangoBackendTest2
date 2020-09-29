from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_phone_number(value):
    print(value)
    if value > 999999999 or value < 100000000:
        print("i am working!")
        raise ValidationError(
            _('%(value)s is not a phone number!!!'),
            params={'value': value},
        )


# def validate_first_and_second_name(value):
#     from .models import Customer
#     if value == Customer.first_name:
#         raise ValidationError(
#             _('%(value)s is not a phone number!!!'),
#             params={'value': value},
#         )
