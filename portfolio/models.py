from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, default="Full Stack Developer")
    bio = models.TextField()
    about = models.TextField()
    profile_image = models.ImageField(upload_to='profile/', blank=True, null=True)
    resume = models.FileField(upload_to='resumes/', blank=True, null=True)
    
    def __str__(self):
        return self.user.username

class Skill(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='skills')
    name = models.CharField(max_length=100)
    percentage = models.IntegerField(default=80)
    category = models.CharField(max_length=100, choices=[
        ('frontend', 'Frontend'),
        ('backend', 'Backend'),
        ('tools', 'Tools'),
        ('other', 'Other')
    ])
    
    class Meta:
        ordering = ['-percentage']

class Project(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='projects')
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    technologies = models.CharField(max_length=300)
    github_url = models.URLField(blank=True)
    live_url = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']