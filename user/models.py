from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    SCHOOLCHILD = 1
    DIRECTOR = 2
    PARENT = 3

    MALE = 1
    FEMALE = 2
    GENDER_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    )
    ROLE_CHOICES = (
        (SCHOOLCHILD, 'Schoolchild'),
        (DIRECTOR, 'Director'),
        (PARENT, 'Parent'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, default=1)
    phone_number = models.CharField(max_length=30, blank=True, null=True, default=None)
    gender = models.PositiveSmallIntegerField(choices=GENDER_CHOICES, blank=True, default=MALE)
    photo = models.ImageField(upload_to='photo/', default='photo/foto.jpg')

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwrgs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
