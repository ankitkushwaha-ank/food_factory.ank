from django.contrib.auth.hashers import make_password, check_password
from django.db import models
from django.utils import timezone
from django.utils.timezone import now


class WebUsers(models.Model):
    username = models.CharField(max_length=25, null=False, blank=False, unique=True)
    password = models.CharField(max_length=128, null=False, blank=False)
    email_id = models.EmailField(max_length=35, null=False, blank=True,default=None,unique=False)
    mob_no = models.CharField(max_length=12, null=True, blank=True)
    user_image = models.FileField(upload_to='user/', max_length=250, null=True, default="/user/default-profile-picture-grey-mal.png")
    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(null=True, blank=True)

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

    def __str__(self):
        return self.username