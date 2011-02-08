# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Setting'
        db.create_table('sitesettings_setting', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('site', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['sites.Site'], unique=True)),
            ('group', self.gf('django.db.models.fields.CharField')(default='default', max_length=20)),
        ))
        db.send_create_signal('sitesettings', ['Setting'])

        # Adding unique constraint on 'Setting', fields ['site', 'group']
        db.create_unique('sitesettings_setting', ['site_id', 'group'])

        # Adding model 'SettingItem'
        db.create_table('sitesettings_settingitem', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('setting', self.gf('django.db.models.fields.related.ForeignKey')(related_name='items', to=orm['sitesettings.Setting'])),
            ('key', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('value', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('in_context', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('sitesettings', ['SettingItem'])


    def backwards(self, orm):
        
        # Removing unique constraint on 'Setting', fields ['site', 'group']
        db.delete_unique('sitesettings_setting', ['site_id', 'group'])

        # Deleting model 'Setting'
        db.delete_table('sitesettings_setting')

        # Deleting model 'SettingItem'
        db.delete_table('sitesettings_settingitem')


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
            'site': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['sites.Site']", 'unique': 'True'})
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
