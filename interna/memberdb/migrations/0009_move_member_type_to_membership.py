# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models

class Migration(DataMigration):

    def forwards(self, orm):
        "Write your forwards methods here."
        for member in orm.Member.objects.all():
            for membership in member.Membership.all():
                membership.category = member.category
                membership.save()

    def backwards(self, orm):
        "Write your backwards methods here."
        for membership in orm.Membership.objects.all():
            member = membership.Member
            member.category = membership.category
            member.save()

    models = {
        u'memberdb.member': {
            'Meta': {'ordering': "(u'name', u'id')", 'object_name': 'Member'},
            'category': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '75'}),
            'github': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '16', 'blank': 'True'}),
            'twitter': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'})
        },
        u'memberdb.memberpayment': {
            'Membership': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'MemberPayment'", 'to': u"orm['memberdb.Membership']"}),
            'Meta': {'object_name': 'MemberPayment'},
            'amount': ('django.db.models.fields.FloatField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'payment_date': ('django.db.models.fields.DateField', [], {}),
            'year': ('django.db.models.fields.CharField', [], {'max_length': '4'})
        },
        u'memberdb.membership': {
            'Member': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'Membership'", 'to': u"orm['memberdb.Member']"}),
            'Meta': {'ordering': "(u'-start', u'-Member__pk')", 'object_name': 'Membership'},
            'category': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            'end': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start': ('django.db.models.fields.DateField', [], {})
        }
    }

    complete_apps = ['memberdb']
    symmetrical = True