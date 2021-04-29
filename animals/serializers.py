from rest_framework import serializers


class GroupSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    scientific_name = serializers.CharField()


class CharacteristicSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    characteristic = serializers.CharField()


class AnimalSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    age = serializers.IntegerField()
    weight = serializers.IntegerField()
    sex = serializers.CharField()

    group = GroupSerializer()
    characteristic_set = CharacteristicSerializer(many=True)
