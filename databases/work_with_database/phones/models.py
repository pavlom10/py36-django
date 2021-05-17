from django.db import models
from django.urls import reverse


class Phone(models.Model):
    name = models.TextField(max_length=255)
    price= models.DecimalField(max_digits=8, decimal_places=2)
    image = models.TextField(null=True, max_length=255)
    release_date = models.DateField(null=True, default=None)
    lte_exists = models.BooleanField(default=False)
    slug = models.SlugField(null=False, unique=True)

    def get_absolute_url(self):
        return reverse('show_product', kwargs={'slug': self.slug})  # new

