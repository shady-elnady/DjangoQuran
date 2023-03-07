from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

from Aya.models import Aya
# Create your mofrom django.utils.text import slugify



class BookMark(models.Model): 
    id = models.AutoField(
        primary_key= True,
        verbose_name= _("ID"),
    )
    user = models.OneToOneField(
        get_user_model,
        on_delete= models.CASCADE,
        related_name= _("BookMark"),
        verbose_name= _("User"),
    )
    aya = models.ForeignKey(
        Aya,
        on_delete= models.CASCADE,
        related_name= _("BookMarks"),
        verbose_name= _("Aya"),
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
    def slug(self) -> str:
        return slugify(f"{self.id}")

    def __str__(self) -> str:
        return f"{self.id}"

    def __decode__(self) -> str:
        return f"{self.id}"

    class Meta:
        verbose_name= _("BookMark")
        verbose_name_plural= _("BookMarks")