# -*- coding: utf-8 -*-
from __future__ import print_function, division, absolute_import, unicode_literals

from datetime import date

from pytest import mark

from .. import models


class TestMembershipModel(object):

    @mark.django_db
    def test_active_memberships(self):
        member = models.Member.objects.create(name='fritzli', email='fritzli@example.com')
        models.Membership.objects.create(Member=member,
                start=date(2013, 10, 10), end=None)
        models.Membership.objects.create(Member=member,
                start=date(2013, 10, 10), end=date(2099, 10, 10))
        assert models.Membership.active.count() == 2
        assert models.Membership.expired.count() == 0

    @mark.django_db
    def test_inactive_memberships(self):
        member = models.Member.objects.create(name='fritzli', email='fritzli@example.com')
        models.Membership.objects.create(Member=member,
                start=date(2013, 10, 10), end=date(2013, 10, 12))
        assert models.Membership.active.count() == 0
        assert models.Membership.expired.count() == 1
