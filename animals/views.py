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
            return Response(status=status.HTTP_400_BAD_REQUEST)

        animal_data = serialized_request.data
        group_data = animal_data.pop("group")
        characteristic_set_data = animal_data.pop("characteristic_set")

        group: Group
        group, _ = Group.objects.get_or_create(**group_data)

        animal: Animal = Animal.objects.create(**animal_data, group=group)

        from .services import create_animal_characteristics

        create_animal_characteristics(animal, characteristic_set_data)

        serialized_animal = AnimalSerializer(animal)

        return Response(
            serialized_animal.data,
            status=status.HTTP_201_CREATED,
        )

    def get(self, request, animal_id=0):
        if animal_id:
            try:
                animal = Animal.objects.get(id=animal_id)
                serialized_animal = AnimalSerializer(animal)
                return Response(
                    serialized_animal.data,
                    status=status.HTTP_200_OK,
                )

            except ObjectDoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)

        animals = Animal.objects.all()
        serialized_animals = AnimalSerializer(animals, many=True)

        return Response(serialized_animals.data, status=status.HTTP_200_OK)

    def delete(self, request, animal_id=0):
        try:
            animal = Animal.objects.get(id=animal_id)
            animal.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
