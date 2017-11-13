# -*- coding: utf-8 -*-
# encoding: utf-8
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Topic(models.Model):
    """用户学习的主题"""
    text = models.CharField(max_length=20)
    data_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """返回学习模型的字符串表示"""
        return self.text