from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=63)
    code = models.CharField(max_length=63)

    def __str__(self):
        return self.name


class Material(models.Model):
    name = models.CharField(max_length=63)

    def __str__(self):
        return self.name


class ProductMaterials(models.Model):
    product = models.ForeignKey(Product, related_name="product_for_product", on_delete=models.CASCADE)
    material_for = models.ForeignKey(Material, on_delete=models.CASCADE, related_name="material_for_product")
    quantity = models.PositiveIntegerField()


class WareHouse(models.Model):
    material_in_warehouse = models.ForeignKey(Material, on_delete=models.CASCADE)
    remainder = models.PositiveIntegerField()
    price = models.PositiveIntegerField()

