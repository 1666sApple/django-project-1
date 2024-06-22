from django.db import models

class Item(models.Model):

    def __str__(self):
        return self.name

    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.CharField(max_length=500, default="https://nolabelatthetable.com/wp-content/uploads/2018/01/IMAGE-COMING-SOON-600x600.png")