from django.db import models
from django.urls import reverse


class Bookmark(models.Model):
    site_name = models.CharField(max_length=200)
    url = models.URLField('Site URL')

    def __str__(self):
        return " Name : " + self.site_name + " ,  Address : " + self.url

    def get_absolute_url(self):
        return reverse('detail', args=[str(self.id)])
        #return reverse('list')