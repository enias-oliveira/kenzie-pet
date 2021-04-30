# Kenzie Pet

## Descrição

<p align="center">Uma API web para ajudar donos de PetShop a guardar dados de animais.</p>

## Tecnologias

- [Django](https://www.djangoproject.com/): Python Web Framework
- [Django REST Framework](https://www.django-rest-framework.org/): Python Toolkit for building Web API

## Endpoints

- `POST /animals/ - Cadastrando um animal:`

```json
// REQUEST
{
  "name": "Bidu",
  "age": 1,
  "weight": 30,
  "sex": "macho",
  "group": {
    "name": "cao",
    "scientific_name": "canis familiaris"
  },
  "characteristic_set": [
    {
      "characteristic": "peludo"
    },
    {
      "characteristic": "medio porte"
    }
  ]
}
```

```json
// RESPONSE STATUS -> HTTP 201
{
  "id": 1,
  "name": "Bidu",
  "age": 1.0,
  "weight": 30.0,
  "sex": "macho",
  "group": {
    "id": 1,
    "name": "cao",
    "scientific_name": "canis familiaris"
  },
  "characteristic_set": [
    {
      "id": 1,
      "characteristic": "peludo"
    },
    {
      "id": 2,
      "characteristic": "medio porte"
    }
  ]
}
```

- `GET /animals/ - Fazendo a leitura dos animais cadastrados:`

```json
// RESPONSE STATUS -> HTTP 200
[
  {
    "id": 1,
    "name": "Bidu",
    "age": 1.0,
    "weight": 30.0,
    "sex": "macho",
    "group": {
      "id": 1,
      "name": "cao",
      "scientific_name": "canis familiaris"
    },
    "characteristic_set": [
      {
        "id": 1,
        "characteristic": "peludo"
      },
      {
        "id": 2,
        "characteristic": "medio porte"
      }
    ]
  },
  {
    "id": 2,
    "name": "Hanna",
    "age": 1.0,
    "weight": 20.0,
    "sex": "femea",
    "group": {
      "id": 2,
      "name": "gato",
      "scientific_name": "felis catus"
    },
    "characteristic_set": [
      {
        "id": 1,
        "characteristic": "peludo"
      },
      {
        "id": 3,
        "characteristic": "felino"
      }
    ]
  }
]
```

- `GET /animals/<int:animal_id>/ - Filtrando animais:`
<p>
Se substituirmos animal_id por um id válido, teremos acesso às informações do animal correspondente.
</p>

```json
// RESPONSE STATUS -> HTTP 200
{
  "id": 1,
  "name": "Bidu",
  "age": 1.0,
  "weight": 30.0,
  "sex": "macho",
  "group": {
    "id": 1,
    "name": "cao",
    "scientific_name": "canis familiaris"
  },
  "characteristic_set": [
    {
      "id": 1,
      "characteristic": "peludo"
    },
    {
      "id": 2,
      "characteristic": "medio porte"
    }
  ]
}
```

<p>
Se usarmos um animal_id que não existe, o sistema deve responder com HTTP 404.
</p>

- `DELETE /animals/<int:animal_id>/ - deletando animais:`

```json
// RESPONSE STATUS -> HTTP 204 (no content)
```

## Autor

Enias Oliveira, um desafio da "Kenzie Academy Brasil"
