# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Removing unique constraint on 'Setting', fields ['site']
        db.delete_unique('sitesettings_setting', ['site_id'])

        # Changing field 'Setting.site'
        db.alter_column('sitesettings_setting', 'site_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sites.Site']))


    def backwards(self, orm):
        
        # Changing field 'Setting.site'
        db.alter_column('sitesettings_setting', 'site_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['sites.Site'], unique=True))

        # Adding unique constraint on 'Setting', fields ['site']
        db.create_unique('sitesettings_setting', ['site_id'])


    models = {
        'sites.site': {
            'Meta': {'ordering': "('domain',)", 'object_name': 'Site', 'db_table': "'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'sitesettings.setting': {
            'Meta': {'unique_together': "(('site', 'group'),)", 'object_name': 'Setting'},
            'group': ('django.db.models.fields.CharField', [], {'default': "'default'", 'max_length': '20'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sites.Site']"})
        },
        'sitesettings.settingitem': {
            'Meta': {'object_name': 'SettingItem'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_context': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'key': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'setting': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'items'", 'to': "orm['sitesettings.Setting']"}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['sitesettings']
