from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db.models import Q
from django.db.models.signals import post_save
from django.dispatch import receiver

from rest_framework.authtoken.models import Token
from PIL import Image
from datetime import date
import calendar
from os.path import join

from .managers import UsersManager
from Languages.models import Language


def upload_to(instance, filename):
    extention= filename.split(".")[-1]
    imgName= getattr(instance, 'name', f'{instance.pk}')
    newName= f"{imgName}.{extention}"    
    return join(f"images/{instance.__class__.__name__}/", newName)



class User(AbstractBaseUser, PermissionsMixin):
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    objects = UsersManager()
    
    email = models.EmailField(
        max_length=200,
        unique=True,
        null=False,
        blank=False,
        verbose_name= _("E-Mail"),
    )
    username = models.CharField(
        max_length=30,
        unique=True,
        null=False,
        blank=False,
        verbose_name= _("User Name"),
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name= _("is Active"),
    )
    is_verified = models.BooleanField(
        default=False,
        verbose_name= _("is Verfied"),
    )
    is_staff = models.BooleanField(
        default=False,
        verbose_name= _("is Staff"),
    )
    is_superuser = models.BooleanField(
        default=False,
        verbose_name= _("is Super User"),
    )

    @property
    def slug(self):
        return slugify(str(self.username))

    def __str__(self):
        return f"{self.username}"

    def __decode__(self):
        return f"{self.username}"    

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    # def get_absolute_url(self):
    #     return reverse("_detail", kwargs={"pk": self.pk})


class Profile(models.Model):
    class Genders(models.TextChoices):
        male = "M", _("Male")
        female = "F", _("Female")
    
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        primary_key= True,
        on_delete=models.CASCADE,
        # related_name= _("Profile"),
        # to_field= "email",
        default= get_user_model(),
        verbose_name= _("User"),
    )
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.",
    )
    phone_number = models.CharField(
        validators=[phone_regex],
        max_length=17,
        blank=True,
        null= True,
        verbose_name= _("Phone Number"),
    ) # Validators should be a list
    full_name = models.CharField(
        max_length=80,
        unique=True,
        blank=True,
        null=True,
        verbose_name=_("Full Name"),
    )
    family_name = models.CharField(
        max_length=15,
        blank=True,
        null=True,
        verbose_name=_("Family Name"),
    )
    birth_date = models.DateField(
        blank=True,
        null=True,
        verbose_name=_("Birth Date"),
    )
    gender = models.CharField(
        max_length= 1,
        choices= Genders.choices,
        null=True,
        blank=True,
        verbose_name=_("Gender"),
    )
    language = models.ForeignKey(
        Language,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name= _("Language"),
    )
    image= models.ImageField(
        upload_to= upload_to,
        null= True,
        blank= True,
        verbose_name= _("Image"),
    )
    created_date= models.DateTimeField(
        auto_now_add=True,
        editable=False,
        verbose_name=_("Created Date"),
    )
    last_updated= models.DateTimeField(
        auto_now=True,
        editable=False,
        blank=True,
        null=True,
        verbose_name=_("Last Update"),
    )
    
    @property
    def age(self) -> dict:
        born = self.birth_date
        calendar.setfirstweekday(calendar.SUNDAY)
        today = date.today()
        if today.month >= born.month:
            year = today.year
        else:
            year = today.year - 1
        age_years = year - born.year
        try:  # raised when birth day is February 29 and the current year is not a leap year
            age_days = (today - (born.replace(year=year))).days
        except ValueError:
            age_days = (today - (born.replace(year=year, day=born.day - 1))).days + 1
        month = born.month
        age_months = 0
        while age_days > calendar.monthrange(year, month)[1]:
            age_days = age_days - calendar.monthrange(year, month)[1]
            if month == 12:
                month = 1
                year += 1
            else:
                month += 1
            age_months += 1
        return {
            "year": age_years,
            "month": age_months,
            "day": age_days,
        }

    @property
    def slug(self):
        return slugify(str(self.user.username))

    def __str__(self):
        return f"{self.user.username}"

    def __decode__(self):
        return f"{self.user.username}"

    class Meta:
        verbose_name = _("Profile")
        verbose_name_plural = _("Profiles")

