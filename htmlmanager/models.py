from django.db import models

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=150)
    username = models.CharField(max_length=150,default="",blank=True)
    site = models.URLField(default="/project/")

    @property
    def index(self):
        return self.files.first().filename

    def __str__(self):
        return self.name


class ProjectFile(models.Model):
    data = models.CharField(max_length=999999)
    project = models.ForeignKey(Project,on_delete=models.CASCADE,related_name="files")
    filename = models.CharField(max_length=80,default="")

    def __str__(self):
        return self.filename + "  :  " + self.project.name
    
