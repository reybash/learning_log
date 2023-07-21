from django.db import models
from django.contrib.auth.models import User


class Topic(models.Model):
    text = models.CharField("Name", max_length=250)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.text


class Entry(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)  # CASCADE means
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "entries"

    # to change the plural name of entries in admin panel from "entry" to "entries".

    def __str__(self):
        # this method is used for displaying objects as strings within Django's Admin site and other parts of
        # the framework
        if self.text.__len__() >= 50:
            return f"{self.text[:50]}..."

        return f"{self.text}"
