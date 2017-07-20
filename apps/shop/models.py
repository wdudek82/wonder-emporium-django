from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=250, db_index=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])


class ProductManager(models.Manager):
    def get_queryset(self):
        return super(ProductManager, self).get_queryset()

    def available(self):
        return self.get_queryset().filter(available=True)


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products')
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    # image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    image = models.ImageField(upload_to='products/', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = ProductManager()

    class Meta:
        ordering = ('-created',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])


@receiver(post_save, sender=Product)
def product_post_save_signal(sender, instance, **kwargs):
    if not instance.image:
        instance.image = 'products/Placeholder.png'
        instance.save()
