from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='profile_images/', default='default_avatar.jpg')
    bio = models.TextField(max_length=500, blank=True)
    
    def __str__(self):
        return f'{self.user.username} Profile'
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
        if self.avatar:
            img = Image.open(self.avatar.path)
            if img.height > 300 or img.width > 300:
                output_size = (300, 300)
                img.thumbnail(output_size)
                img.save(self.avatar.path)

class BlogPost(models.Model):
    DESTINATION_CHOICES = [
        ('europe', 'Europe'),
        ('asia', 'Asia'),
        ('north-america', 'North America'),
        ('south-america', 'South America'),
        ('africa', 'Africa'),
        ('oceania', 'Oceania'),
    ]
    
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    destination = models.CharField(max_length=20, choices=DESTINATION_CHOICES)
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    tags = models.CharField(max_length=200, blank=True)
    is_public = models.BooleanField(default=True)
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()
    
    def tags_list(self):
        return [tag.strip() for tag in self.tags.split(',')] if self.tags else []
    
    def __str__(self):
        return self.title