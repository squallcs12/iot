from django.db import models


class Light(models.Model):
    status = models.BooleanField(default=False)
