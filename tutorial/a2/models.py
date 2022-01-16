from django.db import models


class ModelA(models.Model):
    title_category = models.CharField(max_length=255, default='default-a1')
    a2 = models.CharField(max_length=255, default='default-a2')
    a3 = models.CharField(max_length=255, default='default-a3')
    a4 = models.CharField(max_length=255, default='default-a4')

    def __str__(self):
        return self.title_category


class ModelB(models.Model):
    a1 = models.CharField(max_length=255, default='default-a1')
    a2 = models.CharField(max_length=255, default='default-a2')
    a3 = models.CharField(max_length=255, default='default-a3')
    a4 = models.ForeignKey(ModelA, default=1, on_delete=models.CASCADE)

