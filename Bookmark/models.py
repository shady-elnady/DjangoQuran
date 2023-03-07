from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _


from Aya.models import Aya
# Create your mofrom django.utils.text import slugify



class BookMark(models.Model): 
    id = models.AutoField(
        primary_key= True,
        verbose_name= _("ID"),
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
        verbose_name=_("Time"),
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