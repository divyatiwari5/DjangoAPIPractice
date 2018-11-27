from django.db import models

# Create your models here.

class page_heading(models.Model):
   pName = models.CharField(max_length=100)

   def __str__(self):
       return "{}".format(self.pName)

class pagetagModel(models.Model):
    #page name
    name = models.ForeignKey(page_heading, on_delete=models.CASCADE)
    # page title
    title = models.CharField(max_length=100)
    #page meta desc
    mdesc = models.CharField(max_length=1000)
    #page meta keyword
    mkeyword = models.CharField(max_length=1000)
    #meta schema
    mschema = models.CharField(max_length=1000)
    #meta image
    mimage = models.CharField(max_length=1000)

    def __str__(self):
       return "{} - {}".format(self.title, self.mdesc, self.mkeyword, self.mschema, self.mimage)