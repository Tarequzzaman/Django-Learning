from django.db import models
from datetime import datetime
from django.utils import timezone
import uuid

# Create your models here.







from django.utils.translation import ugettext as translate
from django.utils.timezone import now


class AutoCreatedUpdatedMixin(models.Model):

    created_at = models.DateTimeField(
        verbose_name=translate('created at'),
        unique=False,
        null=True,
        blank=True,
        db_index=True,
    )

    updated_at = models.DateTimeField(
        verbose_name=translate('updated at'),
        unique=False,
        null=True,
        blank=True,
        db_index=True,
    )

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.id or not self.created_at:
            self.created_at = now()
            self.updated_at = self.created_at
        else:
            auto_updated_at_is_disabled = kwargs.pop('disable_auto_updated_at', False)
            if not auto_updated_at_is_disabled:
                self.updated_at = now()
        super(AutoCreatedUpdatedMixin, self).save(*args, **kwargs)



class PriceHistory(AutoCreatedUpdatedMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    volume = models.DecimalField(max_digits=7, decimal_places=3)
    class Meta:
        managed = True
        db_table = 'price_history'
    def __unicode__(self):
            return self.id
    def __str__(self):
        return '{}, {}, {}'.format(self.id, self.price, self.volume)