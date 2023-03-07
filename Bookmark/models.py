from django.db import models
from django.conf import settings
from django.utils.text import slugify
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from Aya.models import Aya
# Create your mofrom django.utils.text import slugify



class BookMark(models.Model): 
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        primary_key= True,
        on_delete=models.CASCADE,
        related_name= _("BookMark"),
        default= get_user_model(),
        verbose_name= _("User"),
    )
    aya = models.ForeignKey(
        Aya,
        on_delete= models.CASCADE,
        related_name= _("BookMarks"),
        verbose_name= _("Aya"),
    )
    created_time= models.DateTimeField(
        auto_now_add=True,
        editable=False,
        verbose_name=_("Created Time"),
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
        return slugify(f"{self.pk}")

    def __str__(self) -> str:
        return f"{self.user.username} > {self.last_updated}"

    def __decode__(self) -> str:
        return f"{self.user.username} > {self.last_updated}"

    class Meta:
        verbose_name= _("BookMark")
        verbose_name_plural= _("BookMarks")