from django.db import models

# Create your models here.
class Experience(models.Model):
    start_year = models.CharField( max_length=50)
    end_year = models.CharField( max_length=50)
    position = models.CharField( max_length=50)
    company = models.CharField( max_length=50)
    location = models.CharField( max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.position
    
    
    
class Education(models.Model):
    start_year = models.CharField( max_length=50)
    end_year = models.CharField( max_length=50)
    institution = models.CharField( max_length=50)
    location = models.CharField( max_length=50)
    subject = models.CharField(max_length=50)
    degree = models.CharField(max_length=50)
    result = models.FloatField()
    description = models.TextField()

    def __str__(self):
        return self.degree
    


class ExtraCurriculum(models.Model):
    year = models.IntegerField()
    event = models.CharField(max_length=50)
    organizer = models.CharField(max_length=50)
    venue = models.CharField(default='', max_length=50)
    role = models.CharField(max_length=50)
    description = models.TextField(default="")

    def __str__(self):
        return self.event

    
    


class ProfessionalSkill(models.Model):
    skills = models.CharField(max_length=50)
    level = models.CharField(max_length=50)

    def __str__(self):
        return self.skills

class ProgrammingLanguage(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Fluency(models.Model):
    language = models.CharField(max_length=50)
    def __str__(self):
        return self.language


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField( max_length=254)
    phone = models.IntegerField()
    message = models.TextField()

    def __str__(self):
        return self.name
    

class Projects(models.Model):
    name = models.CharField(max_length=50)
    link = models.URLField(blank=True, max_length=200)
    desc = models.TextField()
    img = models.ImageField(upload_to='images', height_field=None, width_field=None, max_length=None)

    def __str__(self):
        return self.name
    
    