from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

from Aya.models import Aya
from Sora.models import Sora

# Create your mofrom django.utils.text import slugify


class Language(models.Model):
    id = models.AutoField(
        primary_key= True,
        verbose_name= _("ID"),
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
    symbol = models.CharField(
        max_length= 15,
        unique= True,
        verbose_name= _("Symbol Code"),
    )
    emoji = models.CharField(
        max_length= 1,
        verbose_name= _("Emoji"),
    )
    rtl = models.BooleanField(
        default= False,
        verbose_name= _("Right To Left"),
    )

    @property
    def slug(self) -> str:
        return slugify(f"{self.id}")

    def __str__(self) -> str:
        return f"{self.native}"

    def __decode__(self) -> str:
        return f"{self.native}"

    class Meta:
        verbose_name= _("Language")
        verbose_name_plural= _("Languages")



class AyaLanguage(models.Model):
    language = models.ForeignKey(
        Language,
        on_delete= models.CASCADE,
        related_name= _("Aya"),
        verbose_name= _("Language")
    )
    sora = models.ForeignKey(
        Sora,
        on_delete= models.CASCADE,
        related_name= _("SoraLanguages"),
        verbose_name= _("Sora")
    )
    aya = models.ForeignKey(
        Aya,
        on_delete= models.CASCADE,
        related_name= _("AyaLanguages"),
        verbose_name= _("Aya")
    )
    text = models.TextField(
        verbose_name= _("Text")
    )

    @property
    def slug(self) -> str:
        return slugify(f"{self.pk}")

    def __str__(self) -> str:
        return f"{self.language.symbol} {self.aya.pk}"

    def __decode__(self) -> str:
        return f"{self.language.symbol} {self.aya.pk}"

    class Meta:
        unique_together = (
            "language",
            "aya",
        )
        verbose_name= _("Aya Language")
        verbose_name_plural= _("Aya Languages")