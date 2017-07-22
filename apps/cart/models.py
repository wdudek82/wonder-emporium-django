from django.db import models
from django.contrib.sessions.models import Session
from django.db.models.signals import post_save
from django.dispatch import receiver
from apps.shop.models import Product


class Cart(models.Model):
    product = models.ForeignKey(Product)
    price = models.DecimalField(max_digits=10, decimal_places=2, editable=False, null=True, blank=True)
    quantity = models.PositiveIntegerField(default=0)
    session = models.ForeignKey(Session)

    class Meta:
        unique_together = (('product', 'session'),)

    def __str__(self):
        return '{}:{}:{}:{}'.format(
            self.id, self.product.id, self.product.name, self.price
        )


@receiver(post_save, sender=Cart)
def cart_post_save_signal(sender, instance, created, **kwargs):
    if created:
        instance.price = instance.product.price
        instance.save()
