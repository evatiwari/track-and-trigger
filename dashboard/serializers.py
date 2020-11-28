from rest_framework import serializers
from .models import Inventory, Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('item_name','item_quantity')

class InventorySerializer(serializers.ModelSerializer):
    item_set = ItemSerializer(many = True)
    class Meta:
        model = Inventory
        fields = ('user_name')

    def create(self, validated_data):
        item_validated_data = validated_data.pop('item_set')
        inventory = Inventory.objects.create(**validated_data)
        item_set_serializer = self.fields['item_set']
        for each in item_validated_data:
            each['inventory'] = inventory
        items = item_set_serializer.create(item_validated_data)
        return inventory

