from rest_framework import serializers
from company import models


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = ("name", "code")


class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Material
        fields = ("name", )


class ProductMaterialSerializer(serializers.ModelSerializer):
    product = serializers.StringRelatedField(source="product__name")
    material = serializers.StringRelatedField(source="material__name")

    class Meta:
        model = models.ProductMaterials
        fields = ("product", "material_for", "quantity")


class WarehouseSerializer(serializers.ModelSerializer):
    material_in_warehouse = serializers.StringRelatedField(source="material__name")

    class Meta:
        model = models.WareHouse
        fields = ("material_in_warehouse", "remainder", "price")

