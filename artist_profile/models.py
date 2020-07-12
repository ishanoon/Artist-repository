from django.db import models

# Create your models here.
class Artist_dir(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    profession = models.CharField(max_length=200, null=False, blank=True)
    location = models.CharField(max_length=200, null=False, blank=True)
    twitter = models.CharField(max_length=200, null=False, blank=True)
    instagram = models.CharField(max_length=200, null=False, blank=True)
    
    def __str__(self):
        return self.name

class Artist_profile(models.Model):
    artist = models.ForeignKey(Artist_dir, on_delete=models.SET_NULL,null=True)
    biograpy = models.TextField(blank=True)
    image = models.ImageField(null=True, blank=True)
    
    def __str__(self):
        return self.artist.name
    
    @property
    def imageURl(self):
        try:
             image_link = self.image.url
        except:
            image_link = ""
            return image_link 
    

  
    