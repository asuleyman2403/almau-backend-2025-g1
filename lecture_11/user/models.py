from django.db import models
from django.contrib.auth.models import User


class ResetPassword(models.Model):
    email = models.EmailField(null=False, blank=False, max_length=255)
    token = models.CharField(null=False, blank=False, max_length=255)
    created_at = models.DateTimeField(null=False, auto_now_add=True)

    class Meta:
        verbose_name = 'Reset Password'
        verbose_name_plural = 'Reset Passwords'

    def __str__(self):
        return f'{self.id} {self.email} {self.token} {self.created_at}'