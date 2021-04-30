from .models import Characteristic, Animal


def create_animal_characteristics(animal: Animal, data: list):
    def get_or_create_characteristic(characteristic_data: dict):
        return Characteristic.objects.get_or_create(**characteristic_data)[0]

    characteristics = [
        get_or_create_characteristic(characteristic_data)
        for characteristic_data in data
    ]
    for characteristic in characteristics:
        characteristic.animals.add(animal)
