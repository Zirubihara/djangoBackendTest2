from django.core.exceptions import ValidationError


def validate_anulujkredyt_email(value):
    """
    Validate the email passed is in the domain "@anulujkredyt.pl"
    """
    if not value.endswith("@anulujkredyt.pl"):
        raise ValidationError(
            "Sorry, the email submitted is invalid. All emails have to be registered on this domain only - @anulujkredyt.pl.",
            params={'value': value},
        )
