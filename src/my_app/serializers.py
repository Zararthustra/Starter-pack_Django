from rest_framework import serializers
from .models import MyModel


class MyRetrieveListSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyModel
        fields = ('id', 'name', 'created_at', 'updated_at')


class MyRetrieveDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyModel
        fields = ('id', 'name', 'created_at', 'updated_at')


class MyCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyModel
        fields = ('name',)


class MyUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyModel
        fields = ('name',)
