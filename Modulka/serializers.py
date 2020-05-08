from rest_framework import serializers
from .models import Comment,Post
from . import models

class ArticleSerializer(serializers.ModelSerializer):
    
    class Meta:
        
         model=models.Post
            
         fields = ('id','post_title','post_content','post_author')
    

class CommentSerializer(serializers.ModelSerializer):
    
    class Meta:
        
        model = models.Comment
        
        fields = ('id','name', 'email','body', 'post','active')
    
    
    def create(self, validated_data):
        
        return Comment.objects.create(**validated_data)
