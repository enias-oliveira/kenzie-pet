from .models import Characteristic, Animal


def create_animal_characteristics(animal: Animal, data: list):
    characteristics = [
        Characteristic.objects.create(**characteristic_data)
        for characteristic_data in data
    ]
    for characteristic in characteristics:
        characteristic.animals.add(animal)
