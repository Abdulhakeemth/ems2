import uuid
from django.db import models
from django.utils.translation import ugettext_lazy as _
from decimal import Decimal
from django.core.validators import MinValueValidator
from account.models import Account
from django.utils.timezone import datetime


class BaseModel(models.Model):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id = models.AutoField(primary_key=True)
    date_added = models.DateTimeField(default=datetime.now())
    is_deleted = models.BooleanField(default=False)
    # creator = models.ForeignKey(Account, on_delete=models.CASCADE,default=1)

    class Meta:
        abstract = True

class Mode(models.Model):
    readonly = models.BooleanField(default=False)
    maintenance = models.BooleanField(default=False)
    down = models.BooleanField(default=False)

    class Meta:
        db_table = 'mode'
        verbose_name = _('mode')
        verbose_name_plural = _('mode')
        ordering = ('id',)

    class Admin:
        list_display = ('id', 'readonly', 'maintenance', 'down')

    def __str__(self):
        return str(self.id)
