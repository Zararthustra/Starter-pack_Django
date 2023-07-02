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

## Installation

1. Clone the repo
```bash
git clone https://github.com/Zararthustra/Starter-pack_Django
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Make database migration (in `src`)
```bash
python manage.py makemigrations my_app
```
```bash
python manage.py migrate
```

4. Run server (in `src`)
```bash
python manage.py runserver 0.0.0.0:8000
```
