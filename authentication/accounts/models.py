from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password
from django.utils.translation import gettext_lazy as _

from datetime import datetime
import phonenumbers
# from phonenumbers import carrier
# from phonenumbers.phonenumberutil import number_type
import random
import string

from .managers import CustomUserManager


class CustomUser(AbstractUser):

    username = None
    email = models.EmailField(_("email address"), unique=True)
    phone = models.CharField(max_length=15)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()


    # format phone number to e.164 before saving
    def save(self, *args, **kwargs):

        # self.first_name = self.first_name.capitalize()
        # self.last_name = self.last_name.capitalize()

        if self.phone:
            phone = str(self.phone)
            # if carrier._is_mobile(number_type(phonenumbers.parse(phone_number1))):
            phone_number_parsed = phonenumbers.parse(phone, "KE")
            self.phone = phonenumbers.format_number(phone_number_parsed, phonenumbers.PhoneNumberFormat.E164)

        super().save(*args, **kwargs)