from django.contrib import admin
# import module that contains the database
from .models import djangoClasses
# Register your models here.
# this syntax registers the specified database into the admin site
admin.site.register(djangoClasses)

# once this is complete:
    # in the terminal, enter --> python manage.py makemigrations'
    # --> 'python manage.py migrate'
# Create Objects to add to the database:
    # In the terminal --> 'python manage.py shell'
    # >>> from classApp.models import djangoClasses <-- imports specified database
    # >>> a = djangoClasses(Title='', Course_Number=, Instructor_Name='', Duration=) <-- creates a class object
    # >>> a.save() <-- saves into database
    # >>> djangoClasses.objects.all() <-- Used to list all rows (or objects) stored in the database

# After completing necessary steps in this module:
    # Ensure all changes were migrated in the Terminal
    # Go to settings.py FROM the 'Classes' app (which is the main project app)
    # Under Installed_Apps, add 'classApp', to the list

# NOTE: no urls are needed because /admin/ is already listed by default.