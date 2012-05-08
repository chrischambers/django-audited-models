from django.db import models
from django.utils.translation import ugettext_lazy as _
from django_extensions.db.fields import (
    CreationDateTimeField, ModificationDateTimeField
)
from threaded_multihost.fields import CreatorField, EditorField

def audited_model_factory(related_name='%(class)s'):
    class AuditedModel(models.Model):
        datetime_created = CreationDateTimeField(_('Created'))
        datetime_modified = ModificationDateTimeField(_('Last Modified'))
        creator = CreatorField(
            verbose_name=_('creator'),
            related_name='%s_created' % related_name
        )
        editor  = EditorField(
            verbose_name=_('editor'),
            related_name='%s_last_modified' % related_name
        )

        class Meta(object):
            abstract = True
            get_latest_by = 'datetime_created'
    return AuditedModel

AuditedModel = audited_model_factory()
