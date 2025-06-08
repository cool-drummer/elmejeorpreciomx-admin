from django.db import models

class MercadoToken(models.Model):
    access_token = models.CharField(max_length=100)
    token_type = models.CharField(max_length=100)
    expires_in = models.IntegerField()
    scope = models.CharField(max_length=100)
    user_id = models.IntegerField()
    refresh_token = models.CharField(max_length=100)

    def __str__(self):
        return self.access_token
