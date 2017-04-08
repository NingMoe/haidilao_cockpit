# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
from django.forms import ModelForm
from suit.widgets import AutosizedTextarea
from django.db import models

# Create your models here.
# from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import AbstractUser


class BiCommonPagesu(models.Model):
    # class BI_COMMON_PAGESU(models.Model):
    mstrid = models.CharField(primary_key=True, max_length=32)

    mstrname = models.CharField(max_length=64, blank=True)

    mstraddr = models.CharField(max_length=250, blank=True)
    urladdr = models.CharField(max_length=1000, blank=True)

    def __unicode__(self):
        return self.mstrname

    class Meta:
        managed = True
        # db_table = 'tab_bdata_common_pagesu'
        db_table = 'bi_common_pagesu'
        #         db_table ='tab_bdata_common_pagesu'
        verbose_name = '页面配置'
        verbose_name_plural = '页面配置'


class PagesuDocID(models.Model):
    pageid = models.CharField(primary_key=True, max_length=32)

    documentname = models.CharField(max_length=64, blank=True)
    docid = models.CharField(max_length=50, blank=True)

    def __unicode__(self):
        return self.documentname

    class Meta:
        managed = True
        # db_table = 'tab_bdata_common_pagesu'
        db_table = 'bi__pagesu_docid'
        #         db_table ='tab_bdata_common_pagesu'
        verbose_name = '文档配置'
        verbose_name_plural = '文档配置'

# class ProductForm(ModelForm):
#     class Meta:
#         widgets = {
#             '描述信息':AutosizedTextarea,
#             '描述信息':AutosizedTextarea(attrs={'rows': 3, 'class': 'imput-xlarge'}),
#         }