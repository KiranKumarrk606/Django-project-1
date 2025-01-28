from django.db import models

# this file decides the schema  e=design of the db
# any changes to this file must be folowed by the command 
# python manage.py makemigrations -> to generate required DDL statements to affect the DB 
#  and then 
# pyhton manage.py migrate -> to use these statements to migrate changes to The DB




# Create your models here.
class Product(models.Model):# providing the object attribute for the Product
  name = models.CharField(max_length=200)  # this forms a varchar col in the 'product' table of name "name"
  price = models.PositiveBigIntegerField() #unsigned integer
  desc = models.TextField()  # becomes long or medium text
  stock  = models.PositiveIntegerField(default=1)# stock INT DEFAULT 1 


   # for the imagefield ,sql stores only the relative path of the ,images, the actual image will be stored
   # in the specified media server subfolder in htis case products rest of config is in settings.py
  pic = models.ImageField(upload_to ="product/", null = True)
  def __str__(self):
    return f"product : (self.name)"   # this will print out the name which helps me debug easier 
