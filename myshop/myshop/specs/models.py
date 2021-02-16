from django.db import models

# EAV template. Entity - Product, Attribute - Feature,  Value - Feature value

# Features divided by categories
class CategoryFeature(models.Model):
    category = models.ForeignKey("shop.Category", on_delete=models.CASCADE)
    feature_name = models.CharField(max_length=50)
    unit = models.CharField(max_length=50, blank=True)

    class Meta:
        unique_together = ("category", "feature_name")

    def __str__(self):
        return f"{self.category.name} | {self.feature_name}"


class ProductFeatures(models.Model):
    product = models.ForeignKey("shop.Product", on_delete=models.CASCADE)
    feature = models.ForeignKey(CategoryFeature, on_delete=models.CASCADE)
    value = models.CharField(
        max_length=255,
    )

    def __str__(self):
        return f"Product - {self.product.name} | Feature - {self.feature.feature_name} | Value {self.value}"
