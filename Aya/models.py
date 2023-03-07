from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

from Sora.models import Sora

# Create your mofrom django.utils.text import slugify

class Aya(models.Model):
    id = models.AutoField(
        primary_key= True,
        verbose_name= _("ID")
    )
    soraid = models.ForeignKey(
        Sora,
        on_delete= models.CASCADE,
        related_name= _("Ayat"),
        verbose_name= _("Soraid"),
    )
    ayaid = models.PositiveSmallIntegerField(
        verbose_name= _("Ayaid"),
    )
    page = models.PositiveSmallIntegerField(
        verbose_name= _("Page"),
    )
    quarter = models.SmallIntegerField(
        verbose_name= _("Quarter"),
    )
    hezb = models.PositiveSmallIntegerField(
        verbose_name= _("Hezb"),
    )
    joza = models.PositiveSmallIntegerField(
        verbose_name= _("Joza"),
    )
    sajda = models.BooleanField(
        verbose_name= _("Sajda"),
    )
    text = models.TextField(
        verbose_name= _("Text"),
    )
    uthmanitext = models.TextField(
        verbose_name= _("Uthmani Text"),
    )
    searchtext = models.TextField(
        verbose_name= _("Search Text"),
    )
    quarterstart = models.BooleanField(
        verbose_name= _("Quarter Start"),
    )

    @property
    def slug(self) -> str:
        return slugify(f"{self.pk}")

    def __str__(self) -> str:
        return f"{self.soraid.name} Ayaid > {self.ayaid}"

    def __decode__(self) -> str:
        return f"{self.soraid.name} Ayaid > {self.ayaid}"

    class Meta:
        unique_together = (
            "soraid",
            "ayaid",
        )
        verbose_name= _("Aya")
        verbose_name_plural= _("Ayat")