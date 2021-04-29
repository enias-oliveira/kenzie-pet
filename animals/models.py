from django.db import models


class Group(models.Model):
    name = models.CharField(max_length=255)
    scientific_name = models.CharField(max_length=255)


class Animal(models.Model):
    name = models.CharField(max_length=255)
    age = models.FloatField()
    weight = models.FloatField()
    sex = models.CharField(max_length=255)

    group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True)


class Characteristic(models.Model):
    characteristic = models.CharField(max_length=255)
    animals = models.ManyToManyField(Animal)
