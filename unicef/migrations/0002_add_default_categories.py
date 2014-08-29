# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models


class Migration(DataMigration):

    def forwards(self, orm):
        "Write your forwards methods here."
        #Add Other Site
        from category.models import Category

        if not Category.objects.filter(slug='the-facts').exists():
            category = Category.objects.create(title='The facts',
                                               slug='the-facts',
                                               )
            category.sites.add(1)
        if not Category.objects.filter(slug='treatment').exists():
            category = Category.objects.create(title='Treatment',
                                               slug='treatment',
                                               )
            category.sites.add(1)
        if not Category.objects.filter(slug='safe-burial-practices').exists():
            category = Category.objects.create(title='Safe Burial Practices',
                                               slug='safe-burial-practices',
                                               )
            category.sites.add(1)

    def backwards(self, orm):
        from category.models import Category

        if Category.objects.filter(slug='the-facts').exists():
            Category.objects.get(slug='the-facts').delete()
        if Category.objects.filter(slug='treatment').exists():
            Category.objects.get(slug='treatment').delete()
        if Category.objects.filter(slug='safe-burial-practices').exists():
            Category.objects.get(slug='safe-burial-practices').delete()

    models = {
    }

    complete_apps = ['unicef']
    symmetrical = True
