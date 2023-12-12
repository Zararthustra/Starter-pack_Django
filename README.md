# Starter Pack
> WIP

> A Production ready Django API app starter pack.
> 
> This is a template using Django Rest Framework and some basic CRUD configurations.
> 
> This is made with the aim of creating a new application faster, allowing to focus directly on the core of the new project and not waste unnecessary time setting up tedious code.


## Technologies used

|Usage|Name|Version|
|-|-|-|
|Framework|Django|4.2.2
|Language|Python|3.11.0

## Architecture

- src
  - my_app
    - views
      - base_views.py
      - my_views.py
    - admin.py
    - models.py
    - permissions.py
    - serializers.py
    - services.py
    - tests.py
    - urls.py
  - my_project
    - asgi.py
    - settings.py
    - urls.py
    - wsgi.py
- requirements.txt
- My collection.postman_collection.json

## Specification (OAS v3.1)

- [View Swagger](https://app.swaggerhub.com/apis-docs/ARTHMAYER/api-template/1.0.0)

- [View Yaml](./specification.yml)

## Installation

- Clone the repo
```bash
git clone https://github.com/Zararthustra/Starter-pack_Django
```

- Install dependencies
```bash
pip install -r requirements.txt
```

- Make database migration (in `src`)
```bash
python manage.py makemigrations my_app
```
```bash
python manage.py migrate
```

- Run tests (in `src`)
```bash
python manage.py test my_app --verbosity=2
```

- Run server (in `src`)
```bash
python manage.py runserver 0.0.0.0:8000
```