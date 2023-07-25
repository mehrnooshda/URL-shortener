from django.db import models
import hashlib
from django.contrib.auth.models import AbstractUser


class URL(models.Model):
    shortened_url = models.CharField(max_length=100)
    original_url = models.CharField(max_length=300) # todo: do validation on input url format
    creation_date = models.DateTimeField()
    # user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    def save(self, *args, **kwargs):
        hash_object = hashlib.sha256(self.original_url.encode())
        hashed_url = hash_object.hexdigest()[:8]
        # todo: check that if generated hash is not in db, then save it, otherwise generate another hash
        self.shortened_url = hashed_url
        super().save(*args, **kwargs)
    def __str__(self):
        return self.original_url

