from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.
class Review(models.Model):
    def __str__(self):
        return f"Review by {self.name} <{self.email}>"

    name = models.CharField(max_length=25)
    email = models.EmailField()

    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    review = models.TextField()
