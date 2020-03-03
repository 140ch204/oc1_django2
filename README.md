# Cours Openclassroom Django Disquaire

https://openclassrooms.com/fr/courses/4425076-decouvrez-le-framework-django?status=published

Quelques notes : 

>
>./manage.py runserver
>
> manage.py createsuperuser
>

## Création projet

>
>$ django-admin startproject disquaire_project
>
>
>


## ENV Virtuel 

Création : 

> virtualenv -p python3 env

Activation : 

> source env/bin/activate

Figer la config : 

> pip freeze > requirements.txt

Installer suivant le fichier 

> pip install -r requirements.txt

Desactiver l'ENV virtuel : 

> deactivate

Autres : 

>

> which python

> rm -rf env

>

## Git 

git ignore : 

Rajouter le dossier env/

## Migration 

> 
> ./manage.py makemigrations
>
> ./manage.py migrate
>
> ./manage.py showmigrations
>

## psql

>
> $ createdb -O celinems disquaire
>
>
>
>
>
>
> psql bdd
>
> \l        # Liste des  
>
> \dt       #liste des tables 
>
> \d table
>

settings.py

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql', # on utilise l'adaptateur postgresql
        'NAME': 'disquaire', # le nom de notre base de donnees creee precedemment
        'USER': 'celinems', # attention : remplacez par votre nom d'utilisateur
        'PASSWORD': '',
        'HOST': '',
        'PORT': '5432',
    }
}

>
>django-admin startapp store
>
INSTALLED_APPS = [
    # ...
    'django.contrib.staticfiles',
    'debug_toolbar',
]


## Export Base de donnée

>
> ./manage.py dumpdata store > store/dumps/store.json
>
>


## Console django 


>
> ./manage.py shell
>
> from store.models import Artist, Album
>
>  patrick = Artist(name="Patrick Bruel")
>
> patrick.save()
>
> francis = Artist.objects.create(name="Francis Cabrel")
>
> album = Album.objects.create(title="Sarbacane")
>
> album.artists.add(francis)
>
> Artist.objects.all()
>
> Artist.objects.filter(name="Francis Cabrel")
>
>
>
>