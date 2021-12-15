from django.db import models

# Create your models here.

# Create c class that inherits the class needed to create an SQL table
class djangoClasses(models.Model):
    # id is automatically implemented from django
    # COLUMNS for djangoClasses table
    Title = models.CharField(max_length=50, default="")
    Course_Number = models.IntegerField(max_length=15)
    Instructor_Name = models.CharField(max_length=60, default="")
    Duration = models.FloatField(max_length=10)

    # this method gives any created objects a defined name
    # without this mehtod, any created object will be named "djangoClasses object"
    def __str__(self):
        return self.Title

    # this stores the model manager into variable of your choosing
    # in this case, "objects" was used
    objects = models.Manager()

# Once you have completely created your model, register it by:
# Going to admin.py within the classApp app
# import this current module --> "from .models import djangoClasses"
# syntax --> "admin.site.register(djangoClasses)"























