from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _


from Aya.models import Aya
# Create your mofrom django.utils.text import slugify


class Tafseer(models.Model):
    class TafseerTypes(models.TextChoices):
        type1 = "1", _("Type1")
        type2 = "2", _("Type2")
        type3 = "3", _("Type3")
        type4 = "4", _("Type4")
    
    serial_no = models.AutoField(
        primary_key= True,
        verbose_name= _("Serial Nomber"),
    )
    id = models.PositiveSmallIntegerField(
        verbose_name= _("ID"),
    )
    title = models.CharField(
        max_length= 50,
        verbose_name= _("Tilte"),
    )
    info = models.CharField(
        max_length= 50,
        verbose_name= _("Information"),
    )
    type = models.CharField(
        max_length= 1,
        choices= TafseerTypes.choices,
        verbose_name= _("Type"),
    )
    is_download = models.BooleanField(
        verbose_name= _("Is Download"),
    )
   
    @property
    def slug(self) -> str:
        return slugify(f"{self.pk}")

    def __str__(self) -> str:
        return f"{self.title}"

    def __decode__(self) -> str:
        return f"{self.title}"

    class Meta:
        verbose_name= _("Tafseer")
        verbose_name_plural= _("Tafaseer")