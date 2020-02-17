from django.db import models


class Profile(models.Model):
    name = models.Charfield(max_lengh=256)
