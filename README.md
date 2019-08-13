![](https://i.imgur.com/boCxy9G.jpg)

# What is SkyBeat?

SkyBeat is an application that let's you upload, store, and play all of your music from the cloud. You can now manage and listen to your music from any device, anywhere in the world. 

![](https://i.imgur.com/CJYRsfs.png)

## How does it work?

To get started, first create a new album. When adding an album cover logo, it's best to have a resolution of at least 512x512 and to use common image formats such as JPG, JPEG, or PNG.

![](https://i.imgur.com/lKbnQvo.png)

## Adding Songs

After an album is created you will then be able to add/upload songs. Currently supported file types are WAV, MP3, and OGG.

![](https://i.imgur.com/cunChwS.png)

## My Songs

Once songs are added to an album you are then able to play, favorite, and delete them.

![](https://i.imgur.com/pVMJ54I.png)

## Searching

You can also search for music using the search feature at the top of every page. Any relevant albums will appear at the top of the results page, and the results for individual songs will appear below. 

![](https://i.imgur.com/cunChwS.png)

## You can create account ,login and Logout.
![](https://i.imgur.com/JThKQzG.png)

### Installing Django 

Either install from packages by typing these commands in your terminal
```
sudo apt-get update
sudo apt-get install python-django
```
You can confirm whether its installed or not by typing 
```
django-admin --version
```

Other way is installing by using pip 
```
sudo apt-get update
```
Install pip if you dont have by 
```
sudo apt-get install python-pip
```
Then install django by 
```
sudo pip install django
```

### Running the code 
Just go into the code directory and type 
```
python manage.py runserver
```
"My Music" app will start on 127.0.0.1:8000 (Local Address).
 
### Applying Migrations on the Project 
Migrations are Django’s way of propagating changes you make to your models (adding a field, deleting a model, etc.) into your database schema. They’re designed to be mostly automatic, but you’ll need to know when to make migrations, when to run them, and the common problems you might run into.
Now suppose you want to change Album model and have your's you can simply change the code as you require and then run these commands
```
python manage.py makemigrations
python manage.py migrate 
python manage.py runserver
```
You can use *showmigration*  to list projects migration.
### Have Fun ! 

   
