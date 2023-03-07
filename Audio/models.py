from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

from Qaria.models import Qaria

# Create your mofrom django.utils.text import slugify


class Audio(models.Model):

    class AudioTypes(models.TextChoices):
        Murattal = 0, _("Murattal")
        Mujawwad = 1, _("Mujawwad")

    id = models.AutoField(
        primary_key= True,
        verbose_name= _("ID"),
    )
    qaria = models.ForeignKey(
        Qaria,
        on_delete= models.CASCADE,
        related_name= _("Audios"),
        verbose_name= _("Qaria"),
    )
    type = models.CharField(
        max_length= 50,
        choices= AudioTypes.choices,
        verbose_name= _("Audio Type"),
    )
    audio_url = models.CharField(
        max_length= 100,
        unique= True,
        verbose_name= _("Audio URL"),
    )

    @property
    def slug(self) -> str:
        return slugify(f"{self.id}")

    def __str__(self) -> str:
        return f"{self.qaria.native}"

    def __decode__(self) -> str:
        return f"{self.qaria.native}"

    class Meta:
        verbose_name= _("Audio")
        verbose_name_plural= _("Audios")