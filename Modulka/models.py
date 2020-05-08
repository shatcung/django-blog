from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User

from taggit.managers import TaggableManager
from pytils.translit import slugify
from datetime import datetime

from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

from rest_framework.response import Response
from rest_framework.views import APIView

class PublishedManager(models.Manager):
    
    def get_queryset(self):
        
        return super(PublishedManager, self).get_queryset().filter(post_status='published')


class Post(models.Model):
    
    STATUS_CHOICES = (
        
        ('draft', 'Draft'),
        
        ('published', 'Published'),
        
    )

  
    post_author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Modulka_posts', default=0)
    
    post_content = RichTextUploadingField()
    
    post_title = models.CharField(max_length=200)
   
    post_status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    
    post_type = models.CharField(max_length=20,default='Post')
       
    publish = models.DateTimeField(default=timezone.now)
    
    post_modified = models.DateTimeField(auto_now=True)
    
    slug = models.SlugField(max_length=250,
                            
                            unique=True)
    
    objects = models.Manager()  
    
    published = PublishedManager() 
    
    tags = TaggableManager()

    class Meta:
        
        ordering = ('-publish',)

    def __str__(self):
        
        return self.post_title

    def save(self, *args, **kwargs):
        
        self.slug = slugify(self.post_title)	

        return super(Post, self).save(*args, **kwargs)

    def get_absolute_url(self):
        
        slug=reverse('Modulka:post_detail',
                     
                args = [self.publish.year,
                        
                      self.publish.month,
                        
                      self.publish.day,
                        
                      self.slug
                        
                      ])
        print(slug)
        return reverse('Modulka:post_detail',
                       args=[self.publish.year,
                             
                             self.publish.month,
                             
                             self.publish.day,
                             
                             self.slug
                             
                             ])



class Comment(models.Model):
    
    post = models.ForeignKey(Post,
                             
                             on_delete=models.CASCADE,
                             
                             related_name='comments')
    
    name = models.CharField(max_length=80)
    
    email = models.EmailField()
    
    body = models.TextField()
    
    created = models.DateTimeField(auto_now_add=True)
    
    updated = models.DateTimeField(auto_now=True)
    
    active = models.BooleanField(default=False)
       
    class Meta: 
        
        ordering = ('created',) 
 
    def __str__(self): 
        
        return 'Comment by {} on {}'.format(self.name, self.post)
   
