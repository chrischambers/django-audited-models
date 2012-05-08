from datetime import date
from django.test import TestCase
from nose.tools import *

from django.contrib.auth.models import User
from test_app.models import TestDefaultAuditedModel, TestCustomRelatedName
from threaded_multihost.threadlocals import get_current_user, set_current_user


class DefaultAutditedModelTests(TestCase):

    def setUp(self):
        self.original_user = get_current_user()
        self.user = User.objects.create(username='TestyMcTesterson')
        set_current_user(self.user)
        self.test_instance = TestDefaultAuditedModel.objects.create(name='foo')

    def tearDown(self):
        set_current_user(self.original_user)

    def test_auditing_fields_auto_populated_accurately(self):
        today = date.today()
        assert_equal(self.test_instance.creator, self.user)
        assert_equal(self.test_instance.editor, self.user)

        datetime_created = self.test_instance.datetime_created
        datetime_modified = self.test_instance.datetime_modified
        assert_equal(datetime_created.date(), today)
        assert_equal(datetime_modified.date(), today)

        self.test_instance.save()
        assert_equal(datetime_created, self.test_instance.datetime_created)
        assert_true(datetime_modified < self.test_instance.datetime_modified)
        assert_equal(self.test_instance.creator, self.user)
        assert_equal(self.test_instance.editor, self.user)

    def test_get_latest_by_propagates_to_children(self):
        assert_equal(TestDefaultAuditedModel.objects.latest(), self.test_instance)


class CustomPluralFormTests(TestCase):

    def setUp(self):
        self.original_user = get_current_user()
        self.user = User.objects.create(username='TestyMcTesterson')
        set_current_user(self.user)
        self.test_instance = TestCustomRelatedName.objects.create(name='foo')

    def tearDown(self):
        set_current_user(self.original_user)

    def test_correct_related_field_names(self):
        assert_equal(
            set(self.user.tests_created.all()),
            set(TestCustomRelatedName.objects.all())
        )
        assert_equal(
            set(self.user.tests_last_modified.all()),
            set(TestCustomRelatedName.objects.all())
        )
        self.test_instance.save()
        self.user = User.objects.get(pk=self.user.pk)
        assert_equal(
            set(self.user.tests_last_modified.all()),
            set(TestCustomRelatedName.objects.all())
        )
        assert_equal(
            set(self.user.tests_created.all()),
            set(TestCustomRelatedName.objects.all())
        )
