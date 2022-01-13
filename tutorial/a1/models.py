from django.db import models


class ModelA(models.Model):
    a1 = models.CharField(max_length=255, default='default-a1')
    a2 = models.CharField(max_length=255, default='default-a2')
    a3 = models.CharField(max_length=255, default='default-a3')
    a4 = models.CharField(max_length=255, default='default-a4')
