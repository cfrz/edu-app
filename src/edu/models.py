from django.db import models
from django.utils.encoding import smart_unicode
from tinymce.models import HTMLField


class Prevention(models.Model):
    tag = models.CharField(max_length=25)
    body = HTMLField()
    blurb = HTMLField()
    
    def __unicode__(self):
        return smart_unicode(self.tag)

class Iso(models.Model):
    tag = models.CharField(max_length=15)
    body = HTMLField()
    ppe = models.ManyToManyField(Prevention)
    blurb = HTMLField()
    
    def __unicode__(self):
        return smart_unicode(self.tag)
    
class PathType(models.Model):
    tag = models.CharField(max_length=15)
    body = HTMLField()
    
    def __unicode__(self):
        return smart_unicode(self.tag)
    
    
class Pathogen(models.Model):
    tag = models.CharField(max_length=15)
    id = models.AutoField(primary_key=True)
    sci_name = models.CharField(max_length=40)
    iso_type = models.ForeignKey(Iso)
    path_type = models.ForeignKey(PathType)
    body = HTMLField()
    blurb = HTMLField()
    
    def __unicode__(self):
        return smart_unicode(self.tag)
    
    class Meta:
        ordering = ['tag']
        
class HAI(models.Model):
    tag = models.CharField(max_length=30)
    body = HTMLField()
    
    def __unicode__(self):
        return smart_unicode(self.tag)
    
    hai_def = models.CharField(max_length=200)
    path_type = models.ManyToManyField(Pathogen, null=True, blank=True)
    prev_tags = models.ManyToManyField(Prevention)
    

        
class Article(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False)
    body = HTMLField()
    date = models.DateTimeField(auto_now_add=False, auto_now=True)
    tags = models.ManyToManyField(Pathogen)
    iso_tags = models.ManyToManyField(Iso)
    prev_tags = models.ManyToManyField(Prevention)
    hai_tags = models.ManyToManyField(HAI)
    
    class Meta:
        ordering = ['-date']
        
    def __unicode__(self):
        return smart_unicode(self.title)
 