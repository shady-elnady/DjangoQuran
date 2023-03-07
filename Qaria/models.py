from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

# Create your mofrom django.utils.text import slugify


class Qaria(models.Model):
    id = models.AutoField(
        primary_key= True,
        verbose_name= _("ID"),
    )
    name = models.CharField(
        max_length= 50,
        unique= True,
        verbose_name= _("Name"),
    )
    native = models.CharField(
        max_length= 50,
        unique= True,
        verbose_name= _("Native"),
    )

    @property
    def slug(self) -> str:
        return slugify(f"{self.id}")

    def __str__(self) -> str:
        return f"{self.native}"

    def __decode__(self) -> str:
        return f"{self.native}"

    class Meta:
        verbose_name= _("Qaria")
        verbose_name_plural= _("Quraa")