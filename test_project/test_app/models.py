from django.db import models
from audited_models.models import audited_model_factory, AuditedModel


class TestDefaultAuditedModel(AuditedModel):
    name = models.CharField(blank=True, max_length=255)

    def __unicode__(self):
        return u"%s" % self.name


class TestCustomRelatedName(audited_model_factory(related_name='tests')):
    name = models.CharField(blank=True, max_length=255)

    def __unicode__(self):
        return u"%s" % self.name
