from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

# Create your mofrom django.utils.text import slugify



class Sora(models.Model):
    class DisembarkationPlaces(models.TextChoices):
        Makia = 1 , _("Makia")
        Madania = 2 , _("Madania")

    soraid = models.PositiveSmallIntegerField(
        primary_key= True,
        verbose_name= _("Sora Number"),
    )
    name = models.CharField(
        max_length= 15,
        unique= True,
        verbose_name= _("Name"),
    )
    native = models.CharField(
        max_length= 15,
        unique= True,
        verbose_name= _("Native"),
    )
    place = models.CharField(
        max_length= 1,
        choices= DisembarkationPlaces.choices,
        verbose_name= _("Disembarkation Place"),
    )
    noOfVerses = models.PositiveSmallIntegerField(
        null= True,
        verbose_name= _("number Of Verses"),
    )

    @property
    def slug(self) -> str:
        return slugify(f"{self.pk}")

    def __str__(self) -> str:
        return f"{self.name}"

    def __decode__(self) -> str:
        return f"{self.name}"

    class Meta:
        verbose_name= _("Sora")
        verbose_name_plural= _("Souar")