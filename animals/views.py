from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.exceptions import ObjectDoesNotExist

from .serializers import AnimalSerializer
from .models import Animal, Group


class AnimalView(APIView):
    def post(self, request):
        serialized_request = AnimalSerializer(data=request.data)

        if not serialized_request.is_valid():
            return Response(
                serialized_request.errors,
                status=status.HTTP_400_BAD_REQUEST,
            )

        animal_data = serialized_request.data
        group_data = animal_data.pop("group")
        characteristic_set_data = animal_data.pop(
            "characteristic_set",
        )

        group: Group = Group.objects.create(**group_data)
        animal: Animal = Animal.objects.create(**animal_data, group=group)

        from .services import create_animal_characteristics

        create_animal_characteristics(animal, characteristic_set_data)

        serialized_animal = AnimalSerializer(animal)

        return Response(
            serialized_animal.data,
            status=status.HTTP_201_CREATED,
        )

    def get(self, request, animal_id):
        animals = Animal.objects.all()
        serialized_animals = AnimalSerializer(animals, many=True)

        if animal_id:
            try:
                animal = Animal.objects.get(id=animal_id)
                serialized_animal = AnimalSerializer(animal)
                return Response(serialized_animal.data, status=status.HTTP_200_OK)

            except ObjectDoesNotExist:
                return Response(
                    {"msg": "Invalid animal_id"},
                    status=status.HTTP_404_NOT_FOUND,
                )

        return Response(serialized_animals.data, status=status.HTTP_200_OK)
