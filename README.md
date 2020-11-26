# Before Starting

To run your project on local you need a django environment.
To get a quick and easy one I advice you to download Laragon here : https://laragon.org/ <br><br>

I you want to update views or models you will need to get the basics of DjangoFramework. <br>
Basically you will get everything from there : https://docs.djangoproject.com/en/3.1/<br>
But for french people this guide will be very helpful : https://openclassrooms.com/fr/courses/4425076-decouvrez-le-framework-django

# Creating admin account

Once you have your environment open your terminal and go inside the project folder (where you have the manage.py file)<br>
For laragon it should be like that : 
> C:\laragon\www\lambdaBlog-master

Inside this terminal type this command to create the djangosuperuser which will be the admin of the website : <br>
`$ python manage.py createsuperuser` <br>
You are now able to launche the site in local buuut it wont work atm. (You still need to launch it with the command below) : <br> 
`% python manage.py runserver`

# Creating "Auteur" Role and your first writer

Once you have an admin you need to access to this page : <br>
> http://127.0.0.1:8000/admin/ <br><br>

The first thing that you need to do is creating the "Auteur" group (the writing is really important) by clicking on the "Add" button next to "Groups"<br>
Just write "Auteur" in the name and save it.

Then if you decide that your admin wont be a writer you need to create another User by clicking the "Add" button next to "Users"<br><br>

When you have a writer, click on users and choose him in the list.<br>
In the "Available Groups" section, double click on "Auteur" and save at the bottom of the page.<br><br>

Once its done, go to "Profiles" and create a profile with the User. Set articles to 0 and write the Bio you want (it can be change later)

# Writing the first article to launch the site

In order to get the site working, you need to create the first article in the admin section.<br>
To do that, click on "Articles", select your writer and fill the form before saving it.

