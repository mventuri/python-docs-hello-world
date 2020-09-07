# models.py
from django.db import models

class AboutMe(models.Model):
    title = models.CharField(max_length=60)
    aboutText = models.TextField(max_length=1000)
    def __str__(self):
        return self.title

class TopSkills(models.Model):
    skillName = models.CharField(max_length=100, help_text="Add '#' at the beginning")
    def __str__(self):
        return self.skillName

class Certifications(models.Model):
    name = models.CharField(max_length=100)
    year = models.CharField(max_length=4, default=2020)
    imageName= models.CharField(max_length=50, default="placeholder.png")
    def __str__(self):
        return self.name

class Experience(models.Model):
    company = models.CharField(max_length=100)
    year = models.CharField(max_length=20)
    jobTitle = models.CharField(max_length=200, default="job title")
    description = models.TextField(max_length=2500)
    top_skills = models.ManyToManyField('TopSkills', related_name= 'company')
    
    def __str__(self):
        return self.company

class Education(models.Model):
    course = models.CharField(max_length=100)
    school = models.CharField(max_length=100)
    year = models.CharField(max_length=10, default=2020)
    def __str__(self):
        return self.course
    